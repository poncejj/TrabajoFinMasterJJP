import os
import numpy as np
import pandas as pd
from .util import *
from ..models import *
from .my_classes import *
from django.conf import settings
from ..common import my_constants
from datetime import datetime, date, time, timedelta

def getLocalStores(route_date):
	if settings.TRANSACTIONS is not None and route_date is not None:
		if isinstance(route_date, datetime):
			route_date = route_date.date()
		df = settings.TRANSACTIONS[(settings.TRANSACTIONS.date == str(route_date))]
		store_list = df['store_nbr'].drop_duplicates().values.tolist()
		stores = Store.objects.filter(pk__in = store_list)
		items_list = df['item_nbr'].tolist()
		df2 = pd.DataFrame(list(Item.objects.filter(item_nbr__in = items_list).values('item_nbr', 'perishable')))
		df = df.set_index('item_nbr').join(df2.set_index('item_nbr'))
		df['item_nbr'] = df.index
		print('TOTAL unit_sales: ' + str(df['unit_sales'].sum()) )
		del df2
		local_stores = np.empty(shape=(len(stores),), dtype=object)
		for index, store in enumerate(stores):
			items = df.loc[(df['store_nbr'] == store.id), ('store_nbr', 'item_nbr', 'unit_sales', 'perishable')]
			# items = items.sort_values(by=['unit_sales'])
			items = items.reset_index(drop=True)
			print('Store: ' + str(store.id) + ' Total: ' + str(items['unit_sales'].sum()))
			s = LocalStore(store.id)
			s.setPosition(eval(store.location))
			s.setItems(items)
			s.setDistanceCentral()
			local_stores[index] = s
		
		local_stores = sorted(local_stores, key=lambda x: x.central_distance, reverse=True)
		local_stores = np.array(local_stores)
		return local_stores, store_list

def isWeekendHoliday(route_date):
	holiday = HolidayEvent.objects.filter(date = route_date)
	if holiday or route_date.weekday() > 5:
		return True
	return False

def normalizeWeights(log_search):
    total = log_search.distance_rate + log_search.num_trucks_rate + log_search.staff_cost_rate + log_search.fuel_cost_rate + log_search.delivery_time_rate
    log_search.distance_rate /= total
    log_search.num_trucks_rate /= total
    log_search.staff_cost_rate /= total
    log_search.fuel_cost_rate /= total
    log_search.delivery_time_rate /= total

def initParameters(log_search):
	central_store = Store.objects.get(cluster = 0)
	depot = LocalStore(central_store.id)
	depot.setPosition(eval(central_store.location))
	configuration = Configuration.objects.get(id=1)
	my_constants.CENTRAL_STORE = depot
	my_constants.CONFIGURATION = configuration
	my_constants.POPULATION_SIZE = log_search.population_size
	my_constants.EVOLUTION_ITERATIONS = log_search.number_iterations
	my_constants.MUTATION_RATE = log_search.mutation_rate
	my_constants.CROSSOVER_RATE = log_search.crossing_rate
	my_constants.IS_WEEKEND_HOLIDAY = isWeekendHoliday(log_search.route_date)
	my_constants.DRIVING_TIME = timeToFloat(configuration.duration_driving_time)
	my_constants.BREAK_TIME = timeToFloat(configuration.duration_break_time)
	my_constants.LOAD_TIME = timeToFloat(configuration.duration_load_time)
	my_constants.FAILED_ATTEMPTS_STOP = log_search.failed_attempts_stop
	#Normalize al the weights of the objectives, to have the same proportion
	normalizeWeights(log_search)

def initMetaParameters(log_search):
	my_constants.POPULATION_SIZE_META = log_search.population_size
	my_constants.EVOLUTION_ITERATIONS_META = log_search.number_iterations
	my_constants.MUTATION_RATE_META = log_search.mutation_rate
	my_constants.CROSSOVER_RATE_META = log_search.crossing_rate
	my_constants.FAILED_ATTEMPTS_STOP_META = log_search.failed_attempts_stop