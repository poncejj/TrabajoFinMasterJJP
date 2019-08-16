import os
import numpy as np
import pandas as pd
from ..models import *
from .my_classes import *
from django.conf import settings
from ..common import my_constants
from ..common.util import *
from math import sin, cos, sqrt, atan2, radians
from datetime import datetime, date, time, timedelta

def calulateRouteDistance(visited_stores):
    temp_distance = 0
    last_store = None
    for store in visited_stores:
        if last_store is not None:
            temp_distance += getDistance(last_store, store)
    
    return temp_distance

def getAssignedVehicle(chromosome):
	assigned_vehicles = []
	for route in chromosome:
		assigned_vehicles.append(route.vehicle.id)
	return assigned_vehicles
	
def getAssignedDrivers(chromosome):
	assigned_drivers = []
	for route in chromosome:
		for driver in route.drivers:
			if driver != None:
				assigned_drivers.append(driver.id)
	return assigned_drivers

def getAvailableVehicle(route, assigned_vehicles):
	return Vehicle.objects.filter(vehicle_type__perishable = route.vehicle.vehicle_type.perishable).exclude(pk__in=assigned_vehicles).order_by('?').first()

def getAvailableDriver(route, assigned_drivers):
	if route != None and route.vehicle != None:
		return Driver.objects.filter(driver_license__vehicle_type = route.vehicle.vehicle_type).exclude(pk__in=assigned_drivers).order_by('?').first()

def getRouteTime(route, visited_stores = []):
	total_distance = 0
	if visited_stores == []:
		visited_stores = route.visited_stores

	last_store = None
	total_distance = 0
	for store in visited_stores:
		if last_store is not None:
			total_distance += getDistance(last_store, store)
		last_store = store

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

def calculate_distance(visited_stores):
	last_store = None
	total_distance = 0
	for store in visited_stores:
		if last_store is not None:
			total_distance += getDistance(last_store, store)
		last_store = store
	return total_distance

def createPopulation():
	population = np.empty(int(my_constants.POPULATION_SIZE), dtype=object)
	for i in range(int(my_constants.POPULATION_SIZE)):
		chromosome = createChromosome()
		population[i] = chromosome
	return population

def createChromosome():
	print('CREATE CHROMOSOME!')
	chromosome = []
	assigned_drivers = []
	vehicles = Vehicle.objects.all().order_by('?')
	for index, vehicle in enumerate(vehicles):
		temp_assigned_drivers = []
		route = Route('Route ' + str(index))
		route.setVehicle(vehicle)
		route.initAvaibleCapacity()
		total_time = datetime(1994, 1, 31, 0, 0, 0).time()	
		while total_time <= vehicle.vehicle_type.max_work_time:
			selected_driver = Driver.objects.filter(driver_license__vehicle_type = vehicle.vehicle_type).exclude(pk__in=assigned_drivers).exclude(pk__in=temp_assigned_drivers).order_by('?').first()
			if selected_driver != None:
				temp_assigned_drivers.append(selected_driver.id)
				total_time = addTime([total_time, selected_driver.max_work_time, selected_driver.max_work_extra_time])
			else:
				break

		if total_time >= vehicle.vehicle_type.max_work_time:
			route.addDrivers(Driver.objects.filter(id__in = temp_assigned_drivers)[::1])
			assigned_drivers.extend(temp_assigned_drivers)
			route.rename('Route ' + str(len(chromosome) + 1))
			chromosome.append(route)
	return np.array(chromosome)

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
