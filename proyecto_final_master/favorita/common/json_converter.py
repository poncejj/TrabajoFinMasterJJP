import json
from .my_classes import *
from .util import *
from . import my_constants
from .genethic_functions import *

def getJsonCoordinates(route):
	coordinates = {}
	for store in route.visited_stores:
		coordinates[store.name] = store.pos.getCoordinates()
	
	json_coordinates = json.dumps(coordinates)
	return json_coordinates

def getJsonDrivers(route):
	drivers = {}
	i = 0
	for index, driver in enumerate(route.drivers):
		last = index == len(route.drivers) - 1
		drivers[str(driver)], i = getJsonStoresByDriver(route, driver, route.visited_stores[i:], last)

	json_drivers = json.dumps(drivers)
	print(json_drivers)
	return json_drivers

def getJsonItems(route):
	print(route.items)
	items = (route.items.groupby('store_nbr')
       .apply(lambda x: dict(zip(x['item_nbr'],x['unit_sales'])))
       .to_dict())
	
	json_items = json.dumps(items)
	print(json_items)
	return json_items
 
def getJsonStoresByDriver(route, driver, visited_stores, final = False):
	stores = {}
	visited_stores2 = []
	route_time = 0

	for i, store in enumerate(visited_stores):
		if store == my_constants.CENTRAL_STORE and visited_stores2 != []:
			valid, route_time, distance = getRouteTime(route, visited_stores2)
		
		work_time = timeToFloat(driver.max_work_time)
		extra_work_time = work_time + timeToFloat(driver.max_work_extra_time)
		if final == (False and i == len(visited_stores) - 1) or (route_time >= work_time and route_time <= extra_work_time):
			return json.dumps(stores), i
		
		stores[store.name] = store.pos.getCoordinates()
		visited_stores2.append(store)
	
	del visited_stores2

	json_stores = json.dumps(stores)
	return json_stores, (len(visited_stores) - 1)