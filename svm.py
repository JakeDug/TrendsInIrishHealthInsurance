#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  svm.py
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

from linearRegression import readInList
from sklearn.svm import SVR
import datetime
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

def svm(ListOfDicts, ageGroup, dateToPredict):
	price = readInList(ListOfDicts, ageGroup)
	dateStr = readInList(ListOfDicts, "date")
	dateObj = []


	for i in dateStr:
		x = datetime.datetime.strptime(i[0], '%Y-%m-%d')
		x = [x.toordinal()]
		dateObj.append(x)
	
	price = np.array(price)
	dateObj = np.array(dateObj)
	
	svr = SVR(C=1.0, gamma=1.0)
	svr.fit(dateObj, price)
	
	datePred = datetime.datetime.strptime(dateToPredict, '%Y-%m-%d')
	datePred = [datePred.toordinal()]
	
	pred = svr.predict([datePred])
	
	X_train, X_test, y_train, y_test = train_test_split(
	dateObj, price, train_size = 0.70
	)
	#predict values we already know
	y_pred = []

	for i in X_test:
		x = svr.predict([i])
		y_pred.append(x)


	y_pred_formatted = []
	y_test_formatted = []
	
	for i in y_pred:
		i[0] = round(i[0], 2)
		y_pred_formatted.append(i[0])
		
	
	y_test = y_test.astype(np.float)
	for i in y_test:
		y_test_formatted.append(i[0])
	
	print(type(y_test_formatted[0]))
	
	error = mean_absolute_error(y_test_formatted, y_pred_formatted)
	error = round(error, 2)
	pred[0] = round(pred[0], 2)
	
	result = "SVR = " + str(pred[0]) + " with Mean Absolute Error of " + str(error)
	
	return(result)

def randomForest(ListOfDicts, ageGroup, dateToPredict):
	
	price = readInList(ListOfDicts, ageGroup)
	dateStr = readInList(ListOfDicts, "date")
	dateObj = []


	for i in dateStr:
		x = datetime.datetime.strptime(i[0], '%Y-%m-%d')
		x = [x.toordinal()]
		dateObj.append(x)
	
	price = np.array(price)
	dateObj = np.array(dateObj)
	
	datePred = datetime.datetime.strptime(dateToPredict, '%Y-%m-%d')
	datePred = [datePred.toordinal()]
	
	clf_rf = RandomForestRegressor(n_estimators=50)
	clf_rf.fit(dateObj, price)
	pred = clf_rf.predict([datePred])
	
	X_train, X_test, y_train, y_test = train_test_split(
	dateObj, price, train_size = 0.70
	)
	#predict values we already know
	y_pred = []

	for i in X_test:
		x = clf_rf.predict([i])
		y_pred.append(x)


	y_pred_formatted = []
	y_test_formatted = []
	
	for i in y_pred:
		i[0] = round(i[0], 2)
		y_pred_formatted.append(i[0])
		
	
	y_test = y_test.astype(np.float)
	for i in y_test:
		y_test_formatted.append(i[0])
	
	print(type(y_test_formatted[0]))
	
	error = mean_absolute_error(y_test_formatted, y_pred_formatted)
	error = round(error, 2)
	
	pred[0] = round(pred[0], 2)
	
	result = "Random Forest = " + str(pred[0]) + " with Mean Absolute Error of " + str(error)
	return(result)
