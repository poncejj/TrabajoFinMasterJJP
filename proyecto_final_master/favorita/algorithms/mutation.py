import os
import random
import timeit
import numpy as np
from .repair import *
from ..models import *
from .crossover import *
from ..common.util import *
from ..common.my_classes import *
from ..common import my_constants
from copy import copy, deepcopy

#######################  MUTATION ######################
def mutate(chromosome, stores):
    print('MUTATION BEGINING...')
    count = 0
    
    for route in chromosome:
        old_capacity = route.vehicle.vehicle_type.capacity
        assigned_vehicles = getAssignedVehicle(chromosome)        
        assigned_drivers = getAssignedDrivers(chromosome)
        old_route = deepcopy(route)
        if round(random.uniform(0, 1), 2) <= my_constants.MUTATION_RATE:
            #Change vehicle
            new_vehicle = getAvailableVehicle(route, assigned_vehicles)
            if new_vehicle is not None:
                route.vehicle = new_vehicle

            #Change drivers
            new_drivers = getAvailableDrivers(route, assigned_drivers)
            if new_drivers is not None and len(route.drivers) <= len(new_drivers):
                route.drivers = new_drivers[:len(route.drivers)]

            #If capacity is diferent reassign route
            changeRoute = True 
            if route.vehicle.vehicle_type.capacity != old_capacity:
               changeRoute , route = repair_route(route, stores)
            
            if changeRoute == False:
                route = old_route
        count += 1
        
    return chromosome