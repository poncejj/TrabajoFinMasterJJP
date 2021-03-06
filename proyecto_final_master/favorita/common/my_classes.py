import heapq
import pandas as pd
import numpy as np
from . import my_constants, util
from . import common_functions

##################  CLASES  ######################
class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y      

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ") "

    def x_coor(self):
        return self.x

    def y_coor(self):
        return self.y

    def getCoordinates(self):
        return self.x, self.y

class LocalStore:
    pos = Position(-1,-1)
    items = []
    name = ''
    central_distance = 0

    def __init__(self,name):
        self.name = name
        self.items = []

    def setPosition(self,pos):
        self.pos = Position(pos[0],pos[1])

    def setItems(self, items):
        self.items   = items


    def setDistanceCentral(self):
        if self.pos.x_coor() != -1 and self.pos.y_coor() != -1:
            self.central_distance = common_functions.getDistance(my_constants.CENTRAL_STORE,self)

    def getName(self):
        return self.name
        
    def __str__(self):
        return str(self.name) + ' ' +  str(self.pos) + ' ' +  str(self.central_distance)

    def __repr__(self):
        return str(self)

class Route:
    name = ''
    vehicle = None
    drivers = []
    items = []
    visited_stores = []
    delivery_time = 0
    distance = 0
    speed_limit = 0
    max_work_time = 0
    avaible_capacity = 0
    
    def __init__(self, name):
        self.name = name
        self.visited_stores = [my_constants.CENTRAL_STORE]
        self.drivers = []
        self.distance = 0
        self.delivery_time = 0
        self.items = []
                
    def initAvaibleCapacity(self):
        if self.vehicle != None:
            self.avaible_capacity = self.vehicle.vehicle_type.capacity

    def reduceAvaibleCapacity(self, used_capacity):
        self.avaible_capacity -= used_capacity

    def getAvaibleCapacity(self):
        return self.avaible_capacity

    def addDriver(self, driver):
        self.drivers.append(driver)
    
    def setVehicle(self, vehicle):
        self.vehicle = vehicle
        self.speed_limit = self.vehicle.vehicle_type.max_speed_limit
        self.max_work_time = util.timeToFloat(self.vehicle.vehicle_type.max_work_time)
    
    def setDistance(self, distance):
        self.distance = distance

    def getDistance(self):
        return self.distance

    def setDeliveryTime(self, delivery_time):
        self.delivery_time = delivery_time

    def setFitness(self, fitness):
        self.fitness = fitness

    def addStore(self, store, validate = False):
        last_store = self.visited_stores[-1]
        if last_store is not None and last_store != store:
            self.visited_stores.append(store)
            valid_route_time, delivery_time, distance = common_functions.getRouteTime(self)
            if valid_route_time:
                self.distance = distance
                self.delivery_time = delivery_time
                return True
            else:
                if validate:
                    self.visited_stores.pop()
                return False

    def rename(self, name):
        self.name = name

    def __str__(self):
        return self.name + ': Assigned Vehicle: ' + str(self.vehicle.registration)
    
    def __repr__(self):
        return str(self)

