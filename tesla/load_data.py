#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#############################################
# @Author: jlei1
# @Date:   2020-06-21
# @Last Modified By:   jlei1
# @Last Modified Time: 2020-06-21
#############################################

import json
import sqlite3
import pandas as pd
import requests

from sqlalchemy import create_engine
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from configs import HEADERS, QUERY_LIMIT, EVENT_COUNT_URL, EVENT_DTL_URL

# print(EVENT_DTL_URL)

def dataExtractFrUSGS(url: str = None, **kwargs) -> dict:
	"""
	  URL:  Restful API link without arguments or fixed arguments
	  args: Customized API arguments provided 
	        proposed format key=value

	  return a dict formatted data
	"""
	if kwargs:
		for key in kwargs:
			url += f'&{key}={kwargs[key]}'

	print("Info: calling data from url - " + url)

	response = requests.get(url, headers=HEADERS, verify=False)

	if (response.status_code == 200):
		data = json.loads(response.content)
		return data
	else:
		print(f"Fatal Error: data request failed! API response status code: {response.status_code}")

def dataTransform() -> pd.DataFrame:
	"""
	  This function is business specified, it will transform the data into a pandas readable format 
	  rawdata: data retrieved from USGS API
	"""

	# start load data 
	max_event_num = int(dataExtractFrUSGS(EVENT_COUNT_URL))
	print(f'Info: Total Event Number - {max_event_num}.')

	offset_num = 1
	total_event_num = 0
	event_set = []
	while offset_num - 1 < max_event_num:
		data = dataExtractFrUSGS(EVENT_DTL_URL, offset=offset_num)
		
		features = data['features']
		event_set.extend(features)
		
		total_event_num += len(features)
		offset_num += QUERY_LIMIT

	# double check whether the total number matched
	if (total_event_num < max_event_num):
		print('Warning: events retrieved less than the number of total events.')
		return None

	# reorganize the data properties into pandas dataframe
	df_set = []
	columns = {}
	for event in event_set:
		columns = event['properties']
		columns['id'] = event['id']
		
		# geo_X is longitude, geo_Y is latitude and geo_Z is depth
		columns['geo_type'] = event['geometry']['type']
		columns['geo_X'] = event['geometry']['coordinates'][0]
		columns['geo_Y'] = event['geometry']['coordinates'][1]
		columns['geo_Z'] = event['geometry']['coordinates'][2]

		df_set.append(columns)

	data_set = pd.DataFrame(df_set)
	return data_set

def dataLoad2Sqlite(dataset: pd.DataFrame = None) -> None:

	if dataset.empty:
		print('Fatal Error: No data found.')
		return

	engine = create_engine(f'sqlite:///earthquakes.db', echo=True)
	dataset.to_sql('earthquakes', engine, if_exists='replace')

	return None

if __name__ == '__main__':
	data = dataTransform()
	dataLoad2Sqlite(data)
