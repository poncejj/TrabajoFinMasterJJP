import os
import random
import timeit
import pandas as pd
import numpy as np
from ..models import *
from .crossover import *
from ..common.util import *
from copy import copy, deepcopy
from ..common.my_classes import *
from ..common import my_constants


#######################  MUTATION ######################
def mutate(chromosome, stores):
    print('MUTATION BEGINING...')
    index = random.randint(0, len(chromosome) - 1)
    route = deepcopy(chromosome[index])
    assigned_vehicles = getAssignedVehicle(chromosome)        
    assigned_drivers = getAssignedDrivers(chromosome)        
    oldCapacity = chromosome[index].vehicle.vehicle_type.capacity

    #Change vehicle
    route.vehicle = getAvailableVehicle(route, assigned_vehicles)
    if route.vehicle == None:
    	return chromosome

    #Change of drivers
    num_drivers = len(route.drivers)
    route.drivers = []
    for _ in range(num_drivers):
        driver = getAvailableDriver(route, assigned_drivers)
        if driver != None:
            route.drivers.append(driver)
        else:
            return chromosome

    #If capacity is diferent reassign route
    if route.vehicle.vehicle_type.capacity != oldCapacity:
        route = reassign_route(route, stores)
        
    chromosome[index] = route

    return chromosome