#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#############################################
# @Author: jlei1
# @Date:   2020-06-21
# @Last Modified By:   jlei1
# @Last Modified Time: 2020-06-22
#############################################

import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from configs import QUERY_4_Q6_3

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

def getData(db_file: str = 'earthquakes.db') -> pd.DataFrame:

	res_data = []

	try:
		conn = sqlite3.connect(db_file)
		cur = conn.cursor()
		cur.execute(QUERY_4_Q6_3)
		data = cur.fetchall()

		for x in data:
			row = list(x)
			res_data.append(row)
		
		names = ['mag_level', 'hour_of_day', 'frequency']
		df = pd.DataFrame(res_data)
		df.columns = names
		df[['hour_of_day']] = df[['hour_of_day']].astype(str)
		df[['frequency']] = df[['frequency']].astype(int)

		print(df)
		return df

	except sqlite3.Error as e:
		print(e)

def drawHeatMap(rawdata: pd.DataFrame = None) -> None:

	if rawdata.empty:
		print('Fatal Error: Input data is empty!')
		return

	rawdata = rawdata.pivot('mag_level','hour_of_day','frequency')
	ax = sns.heatmap(rawdata, cmap= "RdBu_r")

	plt.show()

	return None

if __name__ == '__main__':
	data = getData()
	drawHeatMap(data)
