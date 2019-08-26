import os
import timeit
import numpy as np
import pandas as pd
import random
from ..models import *
from .my_classes import *
from ..common.util import *
from . import my_constants
from django.conf import settings
from statistics import mean, median, variance, stdev
from math import sin, cos, sqrt, atan2, radians
from datetime import datetime, date, time, timedelta

############################ DISTANCE #################################
def calculateDistance(visited_stores):
	last_store = None
	total_distance = 0
	for store in visited_stores:
		if last_store is not None:
			total_distance += getDistance(last_store, store)
		last_store = store
	return total_distance

def getDistance(localStore1, localStore2):
	lat1 = radians(localStore1.pos.x)
	lon1 = radians(localStore1.pos.y)
	lat2 = radians(localStore2.pos.x)
	lon2 = radians(localStore2.pos.y)

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	return my_constants.R * c

#######################################################################
############################## VEHICLES ###############################

def getAssignedVehicle(chromosome):
	assigned_vehicles = []
	for route in chromosome:
		assigned_vehicles.append(route.vehicle.id)
	return assigned_vehicles
	
def getAvailableVehicle(route, assigned_vehicles):
	return my_constants.VEHICLES.filter(vehicle_type__perishable = route.vehicle.vehicle_type.perishable).exclude(pk__in=assigned_vehicles).order_by('?').first()

#######################################################################
############################## DRIVERS ################################

def getAssignedDrivers(chromosome):
	assigned_drivers = []
	for route in chromosome:
		for driver in route.drivers:
			if driver != None:
				assigned_drivers.append(driver.id)
	return assigned_drivers


def getAvailableDrivers(route, assigned_drivers):
	if route != None and route.vehicle != None:
		return my_constants.DRIVERS.filter(driver_license__vehicle_type = route.vehicle.vehicle_type).exclude(pk__in=assigned_drivers).order_by('?')

#######################################################################
############################### TIME ##################################

def getRouteTime(route, visited_stores = []):
	total_distance = 0
	if visited_stores == []:
		visited_stores = route.visited_stores

	total_distance = calculateDistance(visited_stores)

	driving_time = total_distance / route.speed_limit
	num_loads = int(len(visited_stores) - 1)
	load_time = my_constants.LOAD_TIME * num_loads
	total_time = driving_time + load_time

	if total_time > my_constants.DRIVING_TIME:
		num_breaks = int (total_time/my_constants.DRIVING_TIME)
		break_time = my_constants.BREAK_TIME * num_breaks
		total_time += break_time

	if total_time <= timeToFloat(route.vehicle.vehicle_type.max_work_time):
		return True, total_time, total_distance
	else:
		return False, total_time, total_distance


#######################################################################
############################ SAVE DATA ################################

def evaluateResults(results, log_search, isMeta = False):
	log_search.min_result = min(results[:,1])
	log_search.max_result = max(results[:,1])
	log_search.mean_result = mean(results[:,1])
	log_search.median_result = median(results[:,1])
	log_search.variance_result = variance(results[:,1])
	log_search.std_result = stdev(results[:,1])

	if isMeta:
		log_search.best_fitness = min(results[:,1])
	return log_search

def updateSelected(routeDate, id=0):
	Log.objects.all().update(selected=False)

	if id > 0:
		log = Log.objects.filter(pk=id)
	else:
		log = Log.objects.filter(fitness_result__gte=0, route_date = routeDate).earliest('fitness_result')

	log.selected = True
	log.save()	

def renameRoutes(chromosome):
	for i, r in enumerate(chromosome):
		r.name = 'Route ' + str(i)
	return chromosome

#######################################################################
############################### STORE #################################

def getStoreById(store_id, stores):
    for store in stores:
        if store.name == store_id:
            return store

#######################################################################
############################### UTIL ##################################

def normalizeWeights(log_search):
    total = log_search.distance_weight + log_search.num_trucks_weight + log_search.staff_cost_weight + log_search.fuel_cost_weight + log_search.delivery_time_weight
    log_search.distance_weight /= total
    log_search.num_trucks_weight /= total
    log_search.staff_cost_weight /= total
    log_search.fuel_cost_weight /= total
    log_search.delivery_time_weight /= total

def isWeekendHoliday(route_date):
	holiday = HolidayEvent.objects.filter(date = route_date)
	if holiday or route_date.weekday() > 5:
		return True
	return False

def getDriverLicense():
	driversLicense = []
	listDL = DriverLicense.objects.all()
	for dl in listDL:
		driversLicense.append([dl, list(dl.vehicle_type.all())])
	return driversLicense