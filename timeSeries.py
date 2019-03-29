#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  timeSeries.py
#  
#  Copyright 2019 Jake Duggan <hipas@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import pandas as pd
import numpy as np
from datetime import datetime

colNames = ["plan_name", "company","adult" ,"young_adult_age_25", "young_adult_age_24", "young_adult_age_23", "young_adult_age_22", "young_adult_age_21", "young_adult_age_20", "young_adult_age_19", "young_adult_age_18", "child_one", "child_two", "child_three", "child_four", "newborn","date"]


def convertToDataFrame(ListOfDicts):
	index = ListOfDicts[0]
	data = [index["plan_name"],index["company"] ,index["adult"] ,index["young_adult_age_25"], index["young_adult_age_24"], index["young_adult_age_23"], index["young_adult_age_22"], index["young_adult_age_21"], index["young_adult_age_20"], index["young_adult_age_19"], index["young_adult_age_18"], index["child_one"], index["child_two"], index["child_three"], index["child_four"], index["newborn"], index["date"]]

	priceDF = pd.DataFrame([data], columns=colNames)
	for selectedDict in range(0,len(ListOfDicts)):
		dictData = ListOfDicts[slectedDict]
		pdConvert = pd.DataFrame.from_dict(dictData)
		priceDF.append(pdConvert)
		
	return priceDF

data = pd.read_csv('insuranceData.csv')
print(data.head())
print(data.dtypes)

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
data = pd.read_csv('insuranceData.csv', parse_dates=['date'], index_col='date',date_parser=dateparse)

print(data.head())

print(data.index)

ts = data["adult"]


