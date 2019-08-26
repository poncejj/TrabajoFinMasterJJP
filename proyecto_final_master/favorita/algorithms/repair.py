import random
import timeit
import numpy as np
from ..common.util import *
from ..common.my_classes import *
from ..common import my_constants
from ..common.common_functions import *

def repair_route(route, stores):
    #print('REASSING ROUTE')
    new_route = Route(route.name)
    new_route.drivers = route.drivers
    new_route.setVehicle(route.vehicle)
    new_route.initAvaibleCapacity()

    #Get selected store
    route.items = np.array(route.items)
    store_ids = np.unique(route.items[:,0])
    np.random.shuffle(store_ids)
    for store_id in store_ids:
        selected_store = getStoreById(store_id, stores)
        temp = route.items[route.items[:, 0] == store_id]
        total_temp = np.sum(temp[:,2])
                
        while total_temp > 0:
            if selected_store is not None and new_route.addStore(selected_store, True):      
                if total_temp <= new_route.getAvaibleCapacity():
                    #print('total added to truck')
                    for row in temp:
                        new_route.items.append(row)
                    new_route.reduceAvaibleCapacity(total_temp)
                    temp = temp[temp[:,0] != store_id]
                    total_temp = 0
                else:
                    #print('partial added to truck')
                    items_added = []
                    for row in temp:
                        if row[2] <= new_route.getAvaibleCapacity():
                            new_route.items.append(row)
                            new_route.reduceAvaibleCapacity(row[2])
                        else:
                            items_added.append(row)
                    temp = temp[temp[:,0] != store_id]
                    temp = np.vstack((temp, items_added))   
                    new_route.reduceAvaibleCapacity(new_route.getAvaibleCapacity())
                
                if new_route.getAvaibleCapacity() <= 0:
                    #print('Restart available capacity')
                    new_route.initAvaibleCapacity()
                    new_route.addStore(my_constants.CENTRAL_STORE)
                
                total_temp = np.sum(temp[:,2])
            else:
                return False, route

    #print('return new route')
    return True, new_route
