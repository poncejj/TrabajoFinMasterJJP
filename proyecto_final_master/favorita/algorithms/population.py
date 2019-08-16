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

    print('Time elapsed: {0}'.format(start_time))
    return population, True

def generateChromosome(pop_stores, chromosome, store_ids):
    totals = dict((key, 0) for key in store_ids)
    counts = dict((key, 0) for key in store_ids)
    while pop_stores.size > 0:
        index_route = random.randint(0, chromosome.size - 1)
        
        selected_route = chromosome[index_route]
        
        if selected_route.visited_stores == []:
            selected_store = pop_stores[0]
        else:
            index_store = random.randint(0, pop_stores.size - 1)
            selected_store = pop_stores[index_store]
            
        temp = selected_store.items[selected_store.items['perishable'] == selected_route.vehicle.vehicle_type.perishable]
        total_temp = temp['unit_sales'].sum()
        total = selected_store.items['unit_sales'].sum()
        
        if total == totals[selected_store.name]:
            counts[selected_store.name] += 1
            if counts[selected_store.name] == len(chromosome):
                chromosome = createChromosome()
                return chromosome, False
        else:
            counts[selected_store.name] = 0

        if total > 0 and total_temp > 0:
            print('Add store to route')
            print('total: ' + str(total))
            print('total_temp: ' + str(total_temp))
            selected_route, selected_store = addStoreToRoute(selected_route, selected_store, temp)
            totals[selected_store.name] = total
            total = selected_store.items['unit_sales'].sum()

        if total <= 0:
            print('Delete store to route')
            pop_stores = np.delete(pop_stores, index_store)
            print('Missing stores: ' + str(len(pop_stores)))
        
        if selected_route.getAvaibleCapacity() <= 0:
            print('Restart available capacity')
            selected_route.initAvaibleCapacity()
            selected_route.addStore(my_constants.CENTRAL_STORE)

    print('Clean Chromosome')
    index_del = []
    for i, r in enumerate(chromosome):
        if r.items.empty:
            index_del.append(i)
        else:
            r.addStore(my_constants.CENTRAL_STORE)
    chromosome = np.delete(chromosome, index_del)
    print('Chromosome: ' + str(chromosome))
    return chromosome, True

def addStoreToRoute(selected_route, selected_store, temp):
    print('Delivery time: ' + str(selected_route.delivery_time))
    print('Available capacity: ' + str(selected_route.getAvaibleCapacity()))
    if selected_route.addStore(selected_store) and selected_route.getAvaibleCapacity() > 0:
        total = temp['unit_sales'].sum()
               
        if total <= selected_route.getAvaibleCapacity():
            print('Total added to truck')
            selected_route.items = pd.concat([selected_route.items, temp])
            selected_route.reduceAvaibleCapacity(total)
            selected_store.items = selected_store.items[selected_store.items['perishable'] != selected_route.vehicle.vehicle_type.perishable]
        else:
            print('Partial added to truck')
            for i in temp.index:
                if selected_route.getAvaibleCapacity() > 0:
                    val = temp.get_value(i,'unit_sales')
                    diference =  selected_route.getAvaibleCapacity() - val
                    if diference >= 0:
                        selected_store.items.set_value( i,'unit_sales',0)
                        selected_route.items.append(selected_store.items.loc[i,:])
                        selected_route.reduceAvaibleCapacity(val)
                    else:
                        selected_store.items.set_value( i,'unit_sales', selected_route.getAvaibleCapacity())
                        selected_route.items.append(selected_store.items.loc[i,:])
                        selected_store.items.set_value( i,'unit_sales',abs(diference))
                        selected_route.reduceAvaibleCapacity(selected_route.getAvaibleCapacity())


        selected_store.items = selected_store.items[selected_store.items['unit_sales'] > 0]
        
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
    print('Time elapsed: {0}'.format(start_time))
    return results
