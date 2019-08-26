import os
import random
import timeit
import pandas as pd
import numpy as np
from .fitness import *
from ..models import *
from ..common.util import *
from copy import copy, deepcopy
from ..common.my_classes import *
from ..common import my_constants

#######################  INIT POPULATION  ##############################
def initPopulation(log_search, stores, store_ids):
    print('INITIALIZE POPULATION')
    start_time = timeit.default_timer()
    population = createPopulation()
    fail_attemps = 0
    #Look chromosomes until is complete the population size
    for i in range(my_constants.POPULATION_SIZE):
        valid_chromosome = False
        while valid_chromosome == False:
            pop_stores = deepcopy(stores)
            #chap2-fenotype-genotype
            population[i], valid_chromosome = generateChromosome(pop_stores, population[i], store_ids)
            if valid_chromosome == False:
                fail_attemps += 1
                if fail_attemps == my_constants.FAILED_ATTEMPTS_STOP:
                    return population, False
            else:
                fail_attemps = 0

    print('Time elapsed in inicializate population: {0}'.format(timeit.default_timer() - start_time))
    return population, True

def createPopulation():
    start_time = timeit.default_timer()
    population = []
    
    for i in range(int(my_constants.POPULATION_SIZE)):
        population.append(createChromosome())
    
    print('Time: {0}'.format(timeit.default_timer() - start_time))
    return population

def createChromosome():
    print('CREATE CHROMOSOME!')
    vehicles = list(my_constants.VEHICLES)
    drivers = list(my_constants.DRIVERS)
    driversLicense = list(my_constants.DRIVER_LICENSE)
   
    random.shuffle(vehicles)
    random.shuffle(drivers)
    
    chromosome = []
    assigned_drivers = []
    count = 0
    for vehicle in vehicles:
        licenses = [x[0] for x in driversLicense if vehicle.vehicle_type in x[1]]
        driversTemp = [x for x in drivers if x.id not in assigned_drivers and x.driver_license in licenses]
        if  len(driversTemp) > 0:
            count += 1
            route = Route('Route ' + str(count))
            route.setVehicle(vehicle)
            route.initAvaibleCapacity()

            work_time = 0
            for driver in driversTemp:
                driver_work_time = timeToFloat(driver.max_work_time)

                if work_time + driver_work_time <= route.max_work_time:
                    route.addDriver(driver)
                    assigned_drivers.append(driver.id)
                    work_time += driver_work_time
                else:
                    break
            chromosome.append(route)
    return np.array(chromosome)

def generateChromosome(pop_stores, chromosome, store_ids):
    totals = dict((key, 0) for key in store_ids)
    counts = dict((key, 0) for key in store_ids)
    start_time = timeit.default_timer()
    while pop_stores.size > 0:
        index_route = random.randint(0, chromosome.size - 1)
        
        selected_route = chromosome[index_route]
        
        if selected_route.visited_stores == [my_constants.CENTRAL_STORE]:
            index_store = 0
        else:
            index_store = random.randint(0, pop_stores.size - 1)
        
        selected_store = pop_stores[index_store]
        temp = selected_store.items[selected_store.items[:, 3] ==  selected_route.vehicle.vehicle_type.perishable]
        total = np.sum(selected_store.items, 0)[2]
        total_temp = np.sum(temp, 0)[2]
        #print('Total: ' + str(total))
        #print('Total Temp ' + str(total_temp))
        #print('Temp Len ' + str(len(temp)))

        if total > 0 and total_temp > 0:
            selected_route, selected_store = addStoreToRoute(selected_route, selected_store, temp)
            
            totals[selected_store.name] = total
            total = np.sum(selected_store.items, 0)[2]

            if total == totals[selected_store.name]:
                counts[selected_store.name] += 1
                if counts[selected_store.name] == len(chromosome):
                    chromosome = createChromosome(vehicles, drivers, driversLicense)
                    return chromosome, False
            else:
                counts[selected_store.name] = 0

        if total <= 0:
            # print('Delete store to route')
            pop_stores = np.delete(pop_stores, index_store)
            # print('Missing stores: ' + str(len(pop_stores)))
        
        if selected_route.getAvaibleCapacity() <= 0:
            #print('Restart available capacity')
            selected_route.initAvaibleCapacity()
            selected_route.addStore(my_constants.CENTRAL_STORE)

    # print('Clean Chromosome')
    index_del = []
    count = 0
    for r in chromosome:
        if r.items == []:
            index_del.append(count)
        else:
            r.addStore(my_constants.CENTRAL_STORE)
        count += 1
    chromosome = np.delete(chromosome, index_del)
    # print('Time elapsed create a chromosome: {0}'.format(timeit.default_timer() - start_time))
    return chromosome, True

def addStoreToRoute(selected_route, selected_store, temp):
    #print('Delivery time: ' + str(selected_route.delivery_time))
    #print('Available capacity: ' + str(selected_route.getAvaibleCapacity()))
    total = np.sum(temp, 0)[2]
    if selected_route.addStore(selected_store, True) and selected_route.getAvaibleCapacity() > 0:
        if total <= selected_route.getAvaibleCapacity():
            #print('Total added to truck')
            for row in temp:
                selected_route.items.append(row)

            selected_route.reduceAvaibleCapacity(total)
            selected_store.items = selected_store.items[selected_store.items[:,3] != selected_route.vehicle.vehicle_type.perishable]
        else:
            #print('Partial added to truck')
            items_added = []
            count = 0
            for row in temp:
                if row[2] <= selected_route.getAvaibleCapacity():
                    selected_route.items.append(row)
                    selected_route.reduceAvaibleCapacity(row[2])
                else:
                    items_added.append(row)
                    
            selected_store.items = selected_store.items[selected_store.items[:,3] != selected_route.vehicle.vehicle_type.perishable]
            selected_store.items = np.vstack((selected_store.items, items_added))
            selected_route.reduceAvaibleCapacity(selected_route.getAvaibleCapacity())
            del items_added
    return selected_route, selected_store

#####################   EVALUATE POPULATION FUNTION   ##############################
#chap2-parent-selection
def evaluatePopulation(population, log_search):
    print("EVALUATE POPULATION...")
    results = []
    start_time = timeit.default_timer()
    for i in range(my_constants.POPULATION_SIZE):
        population[i], fitness = evaluateChromosome(population[i], log_search)
        results.append([population[i], fitness])
    
    results = np.array( results )
    results = results[results[:,1].argsort()]
    print('Time elapsed: {0}'.format(timeit.default_timer() - start_time))
    return results
