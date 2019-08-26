import os
import random
import timeit
import numpy as np
import pandas as pd
from ..models import *
from ..common.util import *
from .genethic_algorithm import *
from ..common.my_classes import *
from ..common import my_constants
from datetime import date

#######################  META MAIN  ##############################
def runMetaAlgorithm(meta_log_search):
    start_time = timeit.default_timer()
    
    initMetaParameters(meta_log_search)
    population = initMetaPopulation(meta_log_search)
    results = evaluateMetaPopulation(population, meta_log_search)
    results = evolutionMetaGeneration(results, meta_log_search)
    print(results)
    meta_log_search = evaluateResults(results, meta_log_search, True)
    meta_log_search.total_time = timeit.default_timer() - start_time
    print('Time elapsed meta algorithm: {0}'.format(meta_log_search.total_time))
    updateSelected(meta_log_search.route_date)
    return meta_log_search

#######################  INIT META POPULATION  ##############################
def initMetaPopulation(meta_log_search):
    print('INITIALIZE META POPULATION')
    start_time = timeit.default_timer()
    #Initialize the population
    population = []
    #Look chromosomes until is complete the population size
    for i in range(my_constants.POPULATION_SIZE_META):
        pop = generateLogObject()
        pop.route_date = meta_log_search.route_date
        population.append(pop)

    print('Time elapsed init meta population: {0}'.format(timeit.default_timer() - start_time))
    return population

#######################  GENERATE META CHROMOSOME  ##############################
def generateLogObject():
    new_log_object = Log()
    
    new_log_object.population_size = random.randint(10, 100)
    new_log_object.number_iterations = random.randint(10, 100)
    new_log_object.crossing_rate = round(random.uniform(0.1, 1), 2)
    new_log_object.mutation_rate = round(random.uniform(0.1, 1), 2)
    new_log_object.failed_attempts_stop = random.randint(1, 10)
    new_log_object.distance_weight = round(random.uniform(0.1, 1), 2)
    new_log_object.num_trucks_weight = round(random.uniform(0.1, 1), 2)
    new_log_object.staff_cost_weight = round(random.uniform(0.1, 1), 2)
    new_log_object.fuel_cost_weight = round(random.uniform(0.1, 1), 2)
    new_log_object.delivery_time_weight = round(random.uniform(0.1, 1), 2)
    return new_log_object

#######################  EVALUATE META POPULATION  ##############################

def evaluateMetaPopulation(population, meta_log_search):
    print("EVALUATE META POPULATION...")
    results = []
    start_time = timeit.default_timer()
    for i in range(my_constants.POPULATION_SIZE_META):
        population[i], fitness_result = evaluateMetaChromosome(population[i], meta_log_search)
        results.append([population[i],  fitness_result])
    
    results = np.array( results )
    results = results[results[:,1].argsort()]
    print('Time elapsed: {0}'.format(timeit.default_timer() - start_time))
    return results

def evaluateMetaChromosome(chromosome, meta_log_search):
    has_solution = False
    while has_solution == False:
        has_solution, route, log_search = runGenethicMultiobjective(chromosome)
        if has_solution:
            log_search.save(force_insert=True)
        else:
            chromosome = generateLogObject()
            chromosome.route_date = meta_log_search.route_date

    return chromosome, log_search.fitness_result

#####################   EVOLUTION FUNTION   ##############################
def evolutionMetaGeneration(results, meta_log_search):
    count = 0
    start_time = timeit.default_timer()
    
    while count < my_constants.EVOLUTION_ITERATIONS_META:
        l = list(range(my_constants.POPULATION_SIZE_META))
        random.shuffle(l)
        ax = results[l.pop()][0]
        bx = results[l.pop()][0]
        
        if round(random.uniform(0, 1), 2) <= my_constants.CROSSOVER_RATE_META:
            c = metaCrossover(ax, bx)
            
            if my_constants.MUTATION_RATE_META == round(random.uniform(0, 1), 2):
                c = metaMutation(c)
            c, result = evaluateMetaChromosome(c, meta_log_search)
            results = np.vstack((results, [c, result]))
            
        count += 1

    results = results[results[:,1].argsort()]
    results = results[:my_constants.POPULATION_SIZE]
    print('Time elapsed meta evolution: {0}'.format(timeit.default_timer() - start_time))
    return results

def metaCrossover(chromosomeA, chromosomeB):
    new_meta_log = MetaLog()
    new_meta_log.route_date = chromosomeA.route_date
    #cross population size
    if random.randint(0, 1) == 1:
        new_meta_log.population_size = chromosomeA.population_size
    else:
        new_meta_log.population_size = chromosomeB.population_size

    #cross number of iterations
    if random.randint(0, 1) == 1:
        new_meta_log.number_iterations = chromosomeA.number_iterations
    else:
        new_meta_log.number_iterations = chromosomeB.number_iterations

    #cross mutation rate
    if random.randint(0, 1) == 1:
        new_meta_log.mutation_rate = chromosomeA.mutation_rate
    else:
        new_meta_log.mutation_rate = chromosomeB.mutation_rate

    #cross crossing rate
    if random.randint(0, 1) == 1:
        new_meta_log.crossing_rate = chromosomeA.crossing_rate
    else:
        new_meta_log.crossing_rate = chromosomeB.crossing_rate

    if random.randint(0, 1) == 1:
        new_meta_log.failed_attempts_stop = chromosomeA.failed_attempts_stop
    else:
        new_meta_log.failed_attempts_stop = chromosomeB.failed_attempts_stop

    if random.randint(0, 1) == 1:
        new_meta_log.num_trucks_weight = chromosomeA.num_trucks_weight
    else:
        new_meta_log.num_trucks_weight = chromosomeB.num_trucks_weight

    if random.randint(0, 1) == 1:
        new_meta_log.num_trucks_weight = chromosomeA.num_trucks_weight
    else:
        new_meta_log.num_trucks_weight = chromosomeB.num_trucks_weight

    if random.randint(0, 1) == 1:
        new_meta_log.staff_cost_weight = chromosomeA.staff_cost_weight
    else:
        new_meta_log.staff_cost_weight = chromosomeB.staff_cost_weight

    if random.randint(0, 1) == 1:
        new_meta_log.fuel_cost_weight = chromosomeA.fuel_cost_weight
    else:
        new_meta_log.fuel_cost_weight = chromosomeB.fuel_cost_weight

    if random.randint(0, 1) == 1:
        new_meta_log.delivery_time_weight = chromosomeA.delivery_time_weight
    else:
        new_meta_log.delivery_time_weight = chromosomeB.delivery_time_weight

    if random.randint(0, 1) == 1:
        new_meta_log.distance_weight = chromosomeA.distance_weight
    else:
        new_meta_log.distance_weight = chromosomeB.distance_weight

    return new_meta_log

def metaMutation(chromosome):
    if random.randint(0, 1) == 0:
        chromosome.population_size = random.randint(10, 10)
    if random.randint(0, 1) == 0:
        chromosome.number_iterations = random.randint(2, 2)
    if random.randint(0, 1) == 0:
        chromosome.crossing_rate = round(random.uniform(0.1, 1), 2)
    if random.randint(0, 1) == 0:
        chromosome.mutation_rate = round(random.uniform(0.1, 1), 2)
    if random.randint(0, 1) == 0:
        chromosome.failed_attempts_stop = random.randint(1, 10)
    if random.randint(0, 1) == 0:
        chromosome.route_date = meta_log_search.route_date
    if random.randint(0, 1) == 0:
        chromosome.distance_weight = round(random.uniform(0.1, 1), 2)
    if random.randint(0, 1) == 0:
        chromosome.num_trucks_weight = round(random.uniform(0.1, 1), 2)
    if random.randint(0, 1) == 0:
        chromosome.staff_cost_weight = round(random.uniform(0.1, 1), 2)
    if random.randint(0, 1) == 0:
        chromosome.fuel_cost_weight = round(random.uniform(0.1, 1), 2)
    if random.randint(0, 1) == 0:
        chromosome.delivery_time_weight = round(random.uniform(0.1, 1), 2)
    return chromosome