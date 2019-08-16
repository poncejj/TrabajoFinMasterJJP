import os
import random
import timeit
import pandas as pd
import numpy as np
from ..models import *
from ..common.util import *
from copy import copy, deepcopy
from ..common.my_classes import *
from ..common import my_constants
from ..common.genethic_functions import *

###################   CROSSOVER    #################################
def crossover(chromosome1, chromosome2, stores):
    print('CROSSOVER')
    index1 = random.randint(0, len(chromosome1) - 1)
    index2 = random.randint(0, len(chromosome2) - 1)
    routeA = deepcopy(chromosome1[index1])
    routeB = deepcopy(chromosome2[index2])
    assigned_vehicles1 = getAssignedVehicle(chromosome1)        
    assigned_vehicles2 = getAssignedVehicle(chromosome2)        
    assigned_drivers1 = getAssignedDrivers(chromosome1)        
    assigned_drivers2 = getAssignedDrivers(chromosome2)        
    oldCapacity1 = chromosome1[index1].vehicle.vehicle_type.capacity
    oldCapacity2 = chromosome2[index2].vehicle.vehicle_type.capacity

    if routeA.vehicle.vehicle_type.perishable == routeB.vehicle.vehicle_type.perishable:
        #Change of vehicles
        if chromosome2[index2].vehicle not in assigned_vehicles1:
            routeA.vehicle = chromosome2[index2].vehicle
        else:
            routeA.vehicle = getAvailableVehicle(routeA, assigned_vehicles1)
        
        if chromosome1[index1].vehicle not in assigned_vehicles2:
            routeB.vehicle = chromosome1[index1].vehicle
        else:
            routeB.vehicle = getAvailableVehicle(routeB, assigned_vehicles2)

        #Change of drivers
        routeA.drivers = []
        for driver in chromosome2[index2].drivers:
            if driver not in assigned_drivers1 and driver.driver_license.vehicle_type == chromosome2[index2].vehicle.vehicle_type:
                routeA.drivers.append(driver)
            else:
                routeA.drivers.append(getAvailableDriver(routeA, assigned_drivers1))
        
        routeB.drivers = []
        for driver in chromosome1[index1].drivers:
            if driver not in assigned_drivers2 and driver.driver_license.vehicle_type == chromosome2[index2].vehicle.vehicle_type:
                routeB.drivers.append(driver)
            else:
                routeB.drivers.append(getAvailableDriver(routeB, assigned_drivers2))

        #If capacity is diferent reassign route
        if routeA.vehicle.vehicle_type.capacity != oldCapacity1:
            routeA = reassign_route(routeA, stores)
        if routeB.vehicle.vehicle_type.capacity != oldCapacity2:
            routeB = reassign_route(routeB, stores)
        
        chromosome1[index1] = routeA
        chromosome2[index2] = routeB

    return chromosome1, chromosome2

def reassign_route(route, stores):
    new_route = Route(route.name)
    new_route.drivers = route.drivers
    new_route.vehicle = route.vehicle
    new_route.initAvaibleCapacity()

    #Get selected store
    store_ids = np.unique(route.items['store_nbr'].values)
    count = 0
    while len(store_ids) > 0:
        store_index = random.randint(0, len(store_ids) - 1)
        store_id = store_ids[store_index]
        selected_store = None
        for store in stores:
            if store.name == store_id:
                selected_store = store
                break

        print('Store: ' + str(store_id))
        temp = route.items[route.items['store_nbr'] == store_id]
        total_temp = temp['unit_sales'].sum()
                
        if selected_store != None and new_route.addStore(selected_store):      
            while total_temp > 0:
                print("Total: " + str(total_temp))
                if total_temp > 0 and total_temp <= new_route.getAvaibleCapacity():
                    print('total added to truck')
                    new_route.items = pd.concat([new_route.items, temp])
                    new_route.reduceAvaibleCapacity(total_temp)
                    temp = temp[temp['store_nbr'] != store_id]
                else:
                    print('partial added to truck')
                    for i in temp.index:
                        if new_route.getAvaibleCapacity() > 0:
                            val = temp.get_value(i,'unit_sales')
                            diference =  new_route.getAvaibleCapacity() - val
                            if diference >= 0:
                                temp.set_value( i,'unit_sales',0)
                                new_route.items.append(temp.loc[i,:])
                                new_route.reduceAvaibleCapacity(val)
                            else:
                                temp.set_value( i,'unit_sales', new_route.getAvaibleCapacity())
                                new_route.items.append(temp.loc[i,:])
                                temp.set_value( i,'unit_sales',abs(diference))
                                new_route.reduceAvaibleCapacity(new_route.getAvaibleCapacity())

                temp = temp[temp['unit_sales'] > 0]
                
                if new_route.getAvaibleCapacity() <= 0:
                    print('Restart available capacity')
                    new_route.initAvaibleCapacity()
                    new_route.addStore(my_constants.CENTRAL_STORE)
                
                total_temp = temp['unit_sales'].sum()
            
            if temp['unit_sales'].sum() == 0:
                del store_ids[store_index]
        else:
            count += 1
            if count == my_constants.FAILED_ATTEMPTS_STOP:
                return False, route

    return True, new_route
