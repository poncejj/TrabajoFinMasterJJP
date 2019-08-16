from ..common import my_constants
from ..common.util import *
from ..common.genethic_functions import *
from decimal import Decimal

#########################   FITNESS FUNCTIONS  ################################## 
#Evaluate the fitness of the distance
def evaluateDistanceObj(chromosome):
    #The distance starts on 0
    distance = 0
    #For each of the chromosome 
    for route in chromosome:
        distance += route.distance
    return distance

#Evaluate the fitness of the number of trucks
def evaluateNumTruksObj(chromosome):
    #Start with 0 trucks
    num_trucks = 0
    #For each route in the solution
    for route in chromosome:
        #If the truck have to visit a store
        if len(route.visited_stores) > 1:
            #Count 1 truck for this solution
            num_trucks += 1
    return num_trucks 

#Evaluate the fitness of the staff cost, need first to evaluate the distance and distance
def evaluateStaffCostObj(chromosome):
    staff_cost = 0
    for route in chromosome:
        visited_stores2 = []
        start = 0

        for d, driver in enumerate(route.drivers):
            for i, store in enumerate(route.visited_stores[start:]):
                if store == my_constants.CENTRAL_STORE and visited_stores2 != []:
                    valid, route_time, distance = getRouteTime(route, visited_stores2)
                
                work_time = timeToFloat(driver.max_work_time)
                extra_work_time = work_time + timeToFloat(driver.max_work_extra_time)
                if (d == len(route.drivers) - 1 and i == len(route.visited_stores) - 1 ) or (route_time >= work_time and route_time <= work_time + extra_work_time):
                    #calculate cost
                    start = i
                    if my_constants.IS_WEEKEND_HOLIDAY:
                        staff_cost += route_time * driver.driver_hour_cost * my_constants.CONFIGURATION.weekend_hour_rate
                    else:
                        normal_cost = driver.max_work_time * driver.driver_hour_cost
                        extra_cost = (route_time - driver.max_work_time ) * driver.driver_hour_cost * my_constants.CONFIGURATION.extra_hour_rate
                        staff_cost += normal_cost + extra_cost


                visited_stores2.append(store)
        
        del visited_stores2

    return staff_cost

#Evaluate the fitness of the fuel cost, need first to evaluate the distance
def evaluateFuelCostObj(chromosome):
    #Fuel cost starts on 0
    fuel_cost = 0
    #For each route in the solution
    for route in chromosome:
        #If the route have a distance
        if route.distance > 0:
            #The route fuel cost is equal to the distance by the fuel price that uses that truck
            #Sum the route fuel cost to total fuel cost 
            fuel_cost += ((route.distance / route.vehicle.vehicle_type.km_per_galon)  * route.vehicle.vehicle_type.fuel_type.price)
    return fuel_cost 

#Evaluate the fitness of the delivery time, need first to evaluate the distance
def evaluateDeliveryTimeObj(chromosome):
    max_delivery_time = 0
    for route in chromosome:
        if route.delivery_time > 0:
            if max_delivery_time < route.delivery_time:
                max_delivery_time = route.delivery_time
    return max_delivery_time

def evaluateChromosome(chromosome, log_search):
    distance = Decimal((evaluateDistanceObj(chromosome)))
    num_trucks = Decimal(evaluateNumTruksObj(chromosome))
    fuel_cost = Decimal(evaluateFuelCostObj(chromosome))
    delivery_time = Decimal(evaluateDeliveryTimeObj(chromosome))
    staff_cost = Decimal(evaluateStaffCostObj(chromosome))
    log_search.distance_rate = Decimal(log_search.distance_rate)
    log_search.num_trucks_rate = Decimal(log_search.num_trucks_rate)
    log_search.fuel_cost_rate = Decimal(log_search.fuel_cost_rate)
    log_search.staff_cost_rate = Decimal(log_search.staff_cost_rate)
    log_search.delivery_time_rate = Decimal(log_search.delivery_time_rate)

    fitness = log_search.distance_rate * distance + log_search.num_trucks_rate * num_trucks + log_search.staff_cost_rate * staff_cost + log_search.fuel_cost_rate * fuel_cost + log_search.delivery_time_rate * delivery_time
    print('fitness: ' + str(fitness))
    return chromosome, fitness

def saveFinalChromosome(chromosome, log_search):
    distance = Decimal(evaluateDistanceObj(chromosome))
    num_trucks = Decimal(evaluateNumTruksObj(chromosome))
    fuel_cost = Decimal(evaluateFuelCostObj(chromosome))
    delivery_time = Decimal(evaluateDeliveryTimeObj(chromosome))
    staff_cost = Decimal(evaluateStaffCostObj(chromosome))
    log_search.distance_rate = Decimal(log_search.distance_rate)
    log_search.num_trucks_rate = Decimal(log_search.num_trucks_rate)
    log_search.fuel_cost_rate = Decimal(log_search.fuel_cost_rate)
    log_search.staff_cost_rate = Decimal(log_search.staff_cost_rate)
    log_search.delivery_time_rate = Decimal(log_search.delivery_time_rate)


    fitness = log_search.distance_rate * distance + log_search.num_trucks_rate * num_trucks + log_search.staff_cost_rate * staff_cost + log_search.fuel_cost_rate * fuel_cost + log_search.delivery_time_rate * delivery_time
    
    log_search.distance_result = distance
    log_search.num_trucks_result = num_trucks
    log_search.fuel_cost_result = fuel_cost
    log_search.delivery_time_result = delivery_time
    log_search.staff_cost_result = staff_cost
    log_search.fitness_result = fitness

    return chromosome, log_search