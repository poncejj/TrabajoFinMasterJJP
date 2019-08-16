import pandas as pd
import numpy as np
from datetime import date

# df_train = pd.read_csv("train.csv", usecols=[1, 2, 3, 4, 5],dtype={'item_nbr': 'int32','store_nbr': 'int8','unit_sales': 'float32','onpromotion': bool,},parse_dates=["date"],skiprows=range(1, 66458909))
# print(df_train)
# df_train2016 = df_train[(df_train['date'] >= '2016-01-01') & (df_train['date'] <= '2016-12-31')]
# print(df_train2016)
# df_train2019 = df_train2016
# df_train2019['date'] = df_train2019['date'].mask(df_train2019['date'].dt.year == 2016, df_train2019['date'] + pd.offsets.DateOffset(year=2019))
# print(df_train2019)
# print("Save train2019.csv")
# df_train2019.to_csv("train2019.csv")
# print("df_chart")
# df_chart = df_train2019.groupby(df_train2019['date'].dt.strftime('%B'))['unit_sales'].sum()
# print("Save chart.csv")
# df_chart.to_csv("chart2019.csv")
from math import sin, cos, sqrt, atan2, radians

lat1 = radians(-0.3553059)
lon1 = radians(-78.4522125)
lat2 = radians(-4.0126104)
lon2 = radians(-79.2041838)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

print((6373.0 * c)/60)