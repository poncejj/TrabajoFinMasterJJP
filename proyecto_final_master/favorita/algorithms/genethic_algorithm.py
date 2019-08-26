import os
import random
import timeit
import pandas as pd
import numpy as np
from .fitness import *
from .population import *
from .crossover import *
from .mutation import *
from ..models import *
from ..common.util import *
from ..common.common_functions import *
from ..common.init_functions import *
from copy import copy, deepcopy
from ..common.my_classes import *
from ..common import my_constants

#######################  MAIN  ##############################
def runGenethicMultiobjective(log_search):
    start_time = timeit.default_timer()
    #chap2-parameters-init
    initParameters(log_search)
    #chap2-parameters-init-stores
    stores, store_ids = getLocalStores(log_search.route_date)
    #chap2-population-init
    population, valid_population = initPopulation(log_search, stores, store_ids)
    if valid_population:
        results = evaluatePopulation(population, log_search)
        results = evolutionGeneration(results, stores, log_search)
        chromosome = results[0][0]
        chromosome = renameRoutes(chromosome)
        log_search = evaluateResults(results, log_search)
        chromosome, log_search = evaluateChromosome(chromosome, log_search, True)    
        log_search.total_time = timeit.default_timer() - start_time
        print('Time elapsed Genethic algo: {0}'.format(log_search.total_time))
        return True, chromosome, log_search
    else:
        chromosome = []
        total_distance = 0
        valid_solution = False
        log_search.errors = 'Too much restrictions, can´t be solved'
        log_search.completed = False
        log_search.total_time = timeit.default_timer() - start_time
        print('Time elapsed: {0}'.format(log_search.total_time))
        return False, [], log_search


#####################   EVOLUTION FUNTION   ##############################
def evolutionGeneration(results, stores, log_search):
    start_time = timeit.default_timer()
    for _ in range(my_constants.EVOLUTION_ITERATIONS):
        l = list(range(0, 9))
        random.shuffle(l)
        ax = results[l.pop()][0]
        bx = results[l.pop()][0]
        a = None
        b = None
        
        a, b = crossover(ax, bx, deepcopy(stores))
            
        if a is not None:
            a = mutate(a, deepcopy(stores))
            a, resultA = evaluateChromosome(a, log_search)
            results = np.vstack((results, [a, resultA]))
        
        if b is not None:
            b = mutate(b, deepcopy(stores))
            b, resultB = evaluateChromosome(b, log_search)
            results = np.vstack((results, [b, resultB]))
        
    results = results[results[:,1].argsort()]
    results = results[:my_constants.POPULATION_SIZE]
    print('Time elapsed evolution: {0}'.format(timeit.default_timer() - start_time))
    return results