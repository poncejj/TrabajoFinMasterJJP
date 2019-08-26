import os
import random
import timeit
import pandas as pd
import numpy as np
from .repair import *
from ..models import *
from ..common.util import *
from ..common.my_classes import *
from ..common import my_constants
from ..common.common_functions import *
from copy import copy, deepcopy

###################   CROSSOVER    #################################
def crossover(chromosomeA, chromosomeB, stores):
    print('CROSSOVER')
    assigned_vehiclesA = getAssignedVehicle(chromosomeA)        
    assigned_vehiclesB = getAssignedVehicle(chromosomeB)        
    assigned_driversA = getAssignedDrivers(chromosomeA)        
    assigned_driversB = getAssignedDrivers(chromosomeB)        
    
    sizeA = len(chromosomeA)
    sizeB = len(chromosomeB)
    size = min(sizeA, sizeB)

    for index in range(size):
        routeA = chromosomeA[index]
        routeB = chromosomeB[index]
        vehicleA = routeA.vehicle
        vehicleB = routeB.vehicle
        driversA = routeA.drivers
        driversB = routeB.drivers

        if vehicleA.vehicle_type.perishable == vehicleB.vehicle_type.perishable and round(random.uniform(0, 1), 2) <= my_constants.CROSSOVER_RATE:
            #Change of vehicles
            if vehicleB not in assigned_vehiclesA:
                routeA.vehicle = vehicleB
            else:
                routeA.vehicle = getAvailableVehicle(routeA, assigned_vehiclesA)
            
            if vehicleA not in assigned_vehiclesB:
                routeB.vehicle = vehicleA
            else:
                routeB.vehicle = getAvailableVehicle(routeB, assigned_vehiclesB)
            
            #Change of drivers A
            if driversB not in assigned_driversA:
                routeA.drivers = driversB
            else:
                new_drivers = getAvailableDrivers(routeA, assigned_driversA)
                if new_drivers is not None and len(driversA) <= len(new_drivers):
                    new_drivers = new_drivers[:len(driversA)]
                    routeA.drivers = new_drivers
                    assigned_driversA.extend(new_drivers)

            #Change of drivers B
            if driversA not in assigned_driversB:
                routeB.drivers = driversA
            else:
                new_drivers = getAvailableDrivers(routeB, assigned_driversB)
                if new_drivers is not None and len(driversb) <= len(new_drivers):
                    new_drivers = new_drivers[:len(driversB)]
                    routeB.drivers = new_drivers
                    assigned_driversB.extend(new_drivers)
            
            #If capacity is diferent reassign route
            addA = True
            addB = True
            if routeA.vehicle.vehicle_type.capacity != vehicleA.vehicle_type.capacity:
                addA, routeA = repair_route(routeA, stores)
            if routeB.vehicle.vehicle_type.capacity != vehicleB.vehicle_type.capacity:
                addB, routeB = repair_route(routeB, stores)
            
            if addA:
                chromosomeA[index] = routeA
            if addB:
                chromosomeB[index] = routeB

    return chromosomeA, chromosomeB