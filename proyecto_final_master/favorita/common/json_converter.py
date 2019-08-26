import json
from .my_classes import *
from .util import *
from . import my_constants
from .common_functions import *

def getJsonData(chromosome):
	start_time = timeit.default_timer()
	coordinates = {}
	items_store = {}
	distances = {}
	drivers = {}

	for route in chromosome:
		#distances
		distances[route.name] = round(calculateDistance(route.visited_stores),2)
		#items
		items = []
		for item in route.items:
			items.append([item[0], item[1], item[2], item[3]])
		items_store[route.name] = items
		#coordinates and store
		store_coordinates = []
		for store in route.visited_stores:
			store_coordinates.append([store.name, store.pos.getCoordinates()])
		coordinates[route.name] = store_coordinates
		#drivers
		route_drivers = []
		for driver in route.drivers:
			route_drivers.append(str(driver))
		drivers[route.name] = route_drivers


	json_coordinates = json.dumps(coordinates)
	json_items = json.dumps(items_store)
	json_distances = json.dumps(distances)
	json_drivers = json.dumps(drivers)
	print('Time elapsed json coordinates: {0}'.format(timeit.default_timer() - start_time))
	return json_coordinates, json_items, json_distances, json_drivers

def getJsonDrivers(chromosome):
	start_time = timeit.default_timer()
	drivers = {}
	for route in chromosome:
		drivers_store = {}
		visited_stores2 = []
		assigned_drivers = route.drivers
		s = 0
	
		for store in route.visited_stores:
			if store == my_constants.CENTRAL_STORE and s > 0:
				valid, route_time, distance = getRouteTime(route, visited_stores2)
				
				if assigned_drivers:
					driver = assigned_drivers.pop()

					work_time = timeToFloat(driver.max_work_time)
					extra_work_time = work_time + timeToFloat(driver.max_work_extra_time)

					if (route_time >= work_time and route_time <= extra_work_time and s < len(route.visited_stores)) or (s == len(route.visited_stores) - 1):
						visited_store_min = []
						for store in visited_stores2:
							visited_store_min.append(["Store " + str(store.name), (store.pos.x, store.pos.y)]) 

						drivers_store[str(driver)] = visited_store_min
						visited_stores2 = []
						visited_store_min = []
				else:
					break

			visited_stores2.append(store)
			s += 1
		drivers[route.name] = drivers_store

	print('Time elapsed json drivers: {0}'.format(timeit.default_timer() - start_time))
	return json_drivers
