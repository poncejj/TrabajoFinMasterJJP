from ..common import my_constants
from ..common.util import *
from ..common.common_functions import *
from decimal import Decimal
#########################   FITNESS FUNCTIONS  ################################## 
#Evaluate the fitness of the distance
def evaluateDistanceObj(chromosome):
    #The distance starts on 0
    distance = 0
    #For each of the chromosome 
    for route in chromosome:
        route.distance = calculateDistance(route.visited_stores)
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
        assigned_drivers = route.drivers
        s = 0
        for store in route.visited_stores:
            #When is the central store or the last store to visit
            if store == my_constants.CENTRAL_STORE and s > 0:
                valid, route_time, distance = getRouteTime(route, visited_stores2)
                
                driver = assigned_drivers[-1]
                
                work_time = timeToFloat(driver.max_work_time)
                extra_work_time = work_time + timeToFloat(driver.max_work_extra_time)
                
                if (route_time >= work_time and route_time <= extra_work_time and s < len(route.visited_stores)) or (s == len(route.visited_stores) - 1):
                    if my_constants.IS_WEEKEND_HOLIDAY:
                        staff_cost += route_time * driver.driver_hour_cost * my_constants.CONFIGURATION.weekend_hour_rate
                    else:
                        normal_cost = work_time * driver.driver_hour_cost
                        extra_cost = (route_time - work_time ) * driver.driver_hour_cost * my_constants.CONFIGURATION.extra_hour_rate
                        staff_cost += normal_cost + extra_cost
                    visited_stores2 = []
                    assigned_drivers = assigned_drivers[:-1]

            visited_stores2.append(store)
            s += 1
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

def evaluateChromosome(chromosome, log_search, final = False):
    distance = Decimal(evaluateDistanceObj(chromosome))
    num_trucks = Decimal(evaluateNumTruksObj(chromosome))
    fuel_cost = Decimal(evaluateFuelCostObj(chromosome))
    delivery_time = Decimal(evaluateDeliveryTimeObj(chromosome))
    staff_cost = Decimal(evaluateStaffCostObj(chromosome))

    fitness = log_search.distance_weight * distance + log_search.num_trucks_weight * num_trucks + log_search.staff_cost_weight * staff_cost + log_search.fuel_cost_weight * fuel_cost + log_search.delivery_time_weight * delivery_time
    print('fitness: ' + str(fitness))
    if final:
        log_search.distance_result = distance
        log_search.num_trucks_result = num_trucks
        log_search.fuel_cost_result = fuel_cost
        log_search.delivery_time_result = delivery_time
        log_search.staff_cost_result = staff_cost
        log_search.fitness_result = fitness
        log_search.completed = True
        return chromosome, log_search
    else:
        return chromosome, fitness
