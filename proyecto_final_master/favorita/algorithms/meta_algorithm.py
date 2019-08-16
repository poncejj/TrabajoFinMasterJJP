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
    best_fitness = results[0][1]
    meta_log_search.best_fitness = best_fitness
    Log.objects.all().update(selected=False)
    log = Log.objects.filter(created_date__gte=date.today(), fitness_result__gte=0, route_date=meta_log_search.route_date).earliest('fitness_result')
    log.selected = True
    log.save()
    meta_log_search.total_time = timeit.default_timer() - start_time
    print('Time elapsed: {0}'.format(meta_log_search.total_time))
    return meta_log_search

#######################  INIT META POPULATION  ##############################
def initMetaPopulation(meta_log_search):
    print('INITIALIZE META POPULATION')
    start_time = timeit.default_timer()
    #Initialize the population
    population = []
    #Look chromosomes until is complete the population size
    for i in range(my_constants.POPULATION_SIZE_META):
        pop = generateMetaChromosome(meta_log_search)
        population.append(pop)

    print('Time elapsed: {0}'.format(start_time))
    return population

#######################  GENERATE META CHROMOSOME  ##############################
def generateMetaChromosome(meta_log_search):
    new_log_object = Log()
    new_log_object.population_size = random.randint(10, 100)
    new_log_object.number_iterations = random.randint(10, 100)
    new_log_object.crossing_rate = round(random.uniform(0, 1), 2)
    new_log_object.mutation_rate = round(random.uniform(0, 1), 2)
    new_log_object.failed_attempts_stop = random.randint(1, 10)
    new_log_object.route_date = meta_log_search.route_date
    new_log_object.distance_rate = round(random.uniform(0, 1), 2)
    new_log_object.num_trucks_rate = round(random.uniform(0, 1), 2)
    new_log_object.staff_cost_rate = round(random.uniform(0, 1), 2)
    new_log_object.delivery_time_rate = round(random.uniform(0, 1), 2)
    return new_log_object

#######################  EVALUATE META POPULATION  ##############################
def evaluateMetaPopulation(population, meta_log_search):
    print("EVALUATE META POPULATION...")
    results = []
    start_time = timeit.default_timer()
    for pop in population:
        pop = evaluateMetaChromosome(pop, meta_log_search)
        print('fitness_result: ' + str(pop.fitness_result))
        results.append([pop, pop.fitness_result])
    print('Time elapsed: {0}'.format(start_time))
    return results

def evaluateMetaChromosome(chromosome, meta_log_search):
    has_solution = False
    while has_solution == False:
        has_solution, routes, chromosome = runGenethicMultiobjective(chromosome)
        if has_solution:
            chromosome.save(force_insert=True)
        else:
            chromosome = generateMetaChromosome(meta_log_search)

    return chromosome

#####################   EVOLUTION FUNTION   ##############################
def evolutionMetaGeneration(results, meta_log_search):
    count = 0
    start_time = timeit.default_timer()
    while count < my_constants.EVOLUTION_ITERATIONS_META:
        l = list(range(0, 9))
        random.shuffle(l)
        ax = results[l.pop()][0]
        bx = results[l.pop()][0]
        if my_constants.CROSSOVER_RATE_META == round(random.uniform(0, 1), 2):
            c = metaCrossover(ax, bx)
            if my_constants.MUTATION_RATE_META == round(random.uniform(0, 1), 2):
                c = metaMutation(c)
                results.append(c, evaluateMetaChromosome(c, meta_log_search))
                results = results[results[:,1].argsort()]
        count += 1

    print('Time elapsed: {0}'.format(start_time))
    return results

def metaCrossover(chromosomeA, chromosomeB):
    new_meta_log = MetaLog()
    new_meta_log.route_date = chromosomeA.route_date
    new_log_object.failed_attempts_stop = random.randint(1, 10)
    new_log_object.route_date = meta_log_search.route_date
    new_log_object.distance_rate = round(random.uniform(0, 1), 2)
    new_log_object.num_trucks_rate = round(random.uniform(0, 1), 2)
    new_log_object.staff_cost_rate = round(random.uniform(0, 1), 2)
    new_log_object.delivery_time_rate = round(random.uniform(0, 1), 2)
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
        new_meta_log.num_trucks_rate = chromosomeA.num_trucks_rate
    else:
        new_meta_log.num_trucks_rate = chromosomeB.num_trucks_rate

    if random.randint(0, 1) == 1:
        new_meta_log.num_trucks_rate = chromosomeA.num_trucks_rate
    else:
        new_meta_log.num_trucks_rate = chromosomeB.num_trucks_rate

    if random.randint(0, 1) == 1:
        new_meta_log.staff_cost_rate = chromosomeA.staff_cost_rate
    else:
        new_meta_log.staff_cost_rate = chromosomeB.staff_cost_rate

    if random.randint(0, 1) == 1:
        new_meta_log.delivery_time_rate = chromosomeA.delivery_time_rate
    else:
        new_meta_log.delivery_time_rate = chromosomeB.delivery_time_rate

    if random.randint(0, 1) == 1:
        new_meta_log.distance_rate = chromosomeA.distance_rate
    else:
        new_meta_log.distance_rate = chromosomeB.distance_rate

    return new_meta_log

def metaMutation(chromosome):
    if random.randint(0, 1) == 1:
        chromosome.population_size = random.randint(1, 100)
    if random.randint(0, 1) == 1:
        chromosome.number_iterations = random.randint(1, 100)
    if random.randint(0, 1) == 1:
        chromosome.crossing_rate = round(random.uniform(0, 1), 2)
    if random.randint(0, 1) == 1:
        chromosome.mutation_rate = round(random.uniform(0, 1), 2)
    if random.randint(0, 1) == 1:
        chromosome.failed_attempts_stop = random.randint(1, 10)
    if random.randint(0, 1) == 1:
        chromosome.route_date = meta_log_search.route_date
    if random.randint(0, 1) == 1:
        chromosome.distance_rate = round(random.uniform(0, 1), 2)
    if random.randint(0, 1) == 1:
        chromosome.num_trucks_rate = round(random.uniform(0, 1), 2)
    if random.randint(0, 1) == 1:
        chromosome.staff_cost_rate = round(random.uniform(0, 1), 2)
    if random.randint(0, 1) == 1:
        chromosome.delivery_time_rate = round(random.uniform(0, 1), 2)
    return chromosome