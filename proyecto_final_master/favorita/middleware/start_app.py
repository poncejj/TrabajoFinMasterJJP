import os
import timeit
import numpy as np
import pandas as pd

from django.conf import settings

def loadTransactionsData():
	start_time = timeit.default_timer()
	if settings.TRANSACTIONS is None:
		print('Loading transactions!')
		settings.TRANSACTIONS = pd.read_csv(os.path.join(settings.LOCAL_BDD, "train2019.csv"), usecols=[1, 2, 3, 4, 5],dtype={'item_nbr': 'int32','store_nbr': 'int8','unit_sales': 'float32','onpromotion': bool,})
	print('Time elapsed: {0}'.format(timeit.default_timer() - start_time))
