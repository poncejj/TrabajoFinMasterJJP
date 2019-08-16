import os
import numpy as np
import pandas as pd
from datetime import datetime, date, time, timedelta

def floatToTime(num_hours):
	return (datetime.min + timedelta(hours=num_hours)).time()

def timeToFloat(time):
	return time.hour + time.minute/60 + time.second/3600

def addTime(timeList):
	total = timedelta()
	for timeobj in timeList:
		d = datetime.combine(date.min, timeobj) - datetime.min
		total += d

	if timedelta() < total and (datetime.min + timedelta()).time() == (datetime.min + total).time():
		total = timedelta(hours=int(23), minutes=int(59), seconds=int(59))
	
	return (datetime.min + total).time()

def create_empty_DataFrame(columns):
    df = pd.DataFrame({name: pd.Series(dtype=t) for name, t in columns})
    cols = [name for name, _ in columns]
    return df[cols]