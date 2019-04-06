#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  machineLearning.py
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
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from graph import createPredictionGraph

def readInList(ListOfDicts, index):
	""" 
	Adds a row from an SQL obj to python dict 
	
	Parameters
	----------
	
	ListOfDicts : list
		List of dicts returned from row2dict function
		
	index : string
		used to get data from the dict where key=index
	Returns
	-------
	**retruns** : list
		a list with values matching the key index
	"""
	price = []
	date = []
	data = dict()
	for row in range(0,len(ListOfDicts)):
		query_data = ListOfDicts[row]
		y = [query_data[index] ]
		price.append(y)

	return price

def linearReg(ListOfDicts, ageGroup, dateToPredict):
	""" 
	Given the users input, trains, tests and evaluates a Linear Regression model. Then predicts a value based on this model
	
	Parameters
	----------
	
	ListOfDicts : List
		List containing one or more dicts. These contain the data that will be used to train the model.
		
	ageGroup : String
		A string relating to an age group stored in the dict. This dictates what prices will be used to train, test and predict.
		
	dateToPredict : String
		A string in a date format Y-m-d. This is converted into an ordinal time format and then used as a input to predict the price with the trained model
	Returns
	-------
	**retruns** : String
		returns a string with the value predicted and the mean absolute error associated with the prediction.
	"""
	price = readInList(ListOfDicts, ageGroup)
	dateStr = readInList(ListOfDicts, "date")
	dateObj = []



	for i in dateStr:
		x = datetime.datetime.strptime(i[0], '%Y-%m-%d')
		x = [x.toordinal()]
		dateObj.append(x)


	reg = linear_model.LinearRegression()
	reg.fit(dateObj, price)
	m=reg.coef_[0]
	b=reg.intercept_
	print("slope=", m, "intercept=", b)
	
	#score = reg.score(dateObj, price)


	datePred = datetime.datetime.strptime(dateToPredict, '%Y-%m-%d')
	datePred = [datePred.toordinal()]

	pred = reg.predict(X=[datePred])
	
	X_train, X_test, y_train, y_test = train_test_split(
	dateObj, price, train_size = 0.70
	)
	
	#predict values we already know
	y_pred = []
	print(X_test[0][0])
	
	for i in X_test:
		x = reg.predict(i[0])
		y_pred.append(x[0])

	y_pred_formatted = []
	y_test_formatted = []
	
	for i in y_pred:
		i[0] = round(i[0], 2)
		y_pred_formatted.append(i[0])
	
	for i in y_test:
		i[0] = float(i[0])
		y_test_formatted.append(i[0])
		
	
	print(type(y_test_formatted[0]))
	
	error = mean_absolute_error(y_test_formatted, y_pred_formatted)
	
	error = round(error, 2)
	
	price.append(pred[0][0])
	dateToPredict = [dateToPredict]
	dateStr.append(dateToPredict)

	createPredictionGraph(price, dateStr)
	print(pred[0])
	pred[0][0] = round(pred[0][0], 2)
	
	result = "Linear Regression = " + str(pred[0][0]) + " with Mean Absolute Error of " + str(error)
	return(result)

def svm(ListOfDicts, ageGroup, dateToPredict):
	""" 
	Given the users input, trains, tests and evaluates a SVM model. Then predicts a value based on this model
	
	Parameters
	----------
	
	ListOfDicts : List
		List containing one or more dicts. These contain the data that will be used to train the model.
		
	ageGroup : String
		A string relating to an age group stored in the dict. This dictates what prices will be used to train, test and predict.
		
	dateToPredict : String
		A string in a date format Y-m-d. This is converted into an ordinal time format and then used as a input to predict the price with the trained model
	Returns
	-------
	**retruns** : String
		returns a string with the value predicted and the mean absolute error associated with the prediction.
	"""
	price = readInList(ListOfDicts, ageGroup)
	dateStr = readInList(ListOfDicts, "date")
	dateObj = []


	for i in dateStr:
		x = datetime.datetime.strptime(i[0], '%Y-%m-%d')
		x = [x.toordinal()]
		dateObj.append(x)
	
	priceAxis = price
	dateAxis = dateStr
	
	price = np.array(price)
	dateObj = np.array(dateObj)
	
	svr = SVR(C=1.0, gamma=1.0)
	svr.fit(dateObj, price)
	
	datePred = datetime.datetime.strptime(dateToPredict, '%Y-%m-%d')
	datePred = [datePred.toordinal()]
	
	pred = svr.predict([datePred])
	
	priceAxis.append(pred[0])
	dateToPredict = [dateToPredict]
	dateAxis.append(dateToPredict)
	
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
	
	createPredictionGraph(priceAxis, dateAxis)
	return(result)

def randomForest(ListOfDicts, ageGroup, dateToPredict):
	""" 
	Given the users input, trains, tests and evaluates a Random Forest model. Then predicts a value based on this model.
	
	Parameters
	----------
	
	ListOfDicts : List
		List containing one or more dicts. These contain the data that will be used to train the model.
		
	ageGroup : String
		A string relating to an age group stored in the dict. This dictates what prices will be used to train, test and predict.
		
	dateToPredict : String
		A string in a date format Y-m-d. This is converted into an ordinal time format and then used as a input to predict the price with the trained model
	Returns
	-------
	**retruns** : String
		returns a string with the value predicted and the mean absolute error associated with the prediction.
	"""
	price = readInList(ListOfDicts, ageGroup)
	dateStr = readInList(ListOfDicts, "date")
	dateObj = []


	for i in dateStr:
		x = datetime.datetime.strptime(i[0], '%Y-%m-%d')
		x = [x.toordinal()]
		dateObj.append(x)
		
	priceAxis = price
	dateAxis = dateStr
	
	price = np.array(price)
	dateObj = np.array(dateObj)
	
	datePred = datetime.datetime.strptime(dateToPredict, '%Y-%m-%d')
	datePred = [datePred.toordinal()]
	
	rf = RandomForestRegressor(n_estimators=50)
	rf.fit(dateObj, price)
	pred = rf.predict([datePred])
	
	priceAxis.append(pred[0])
	dateToPredict = [dateToPredict]
	dateAxis.append(dateToPredict)
	
	X_train, X_test, y_train, y_test = train_test_split(
	dateObj, price, train_size = 0.70
	)
	#predict values we already know
	y_pred = []

	for i in X_test:
		x = rf.predict([i])
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
	createPredictionGraph(priceAxis, dateAxis)
	return(result)

def gradientBoostingRegressor(ListOfDicts, ageGroup, dateToPredict):
	""" 
	Given the users input, trains, tests and evaluates a Gradient Boosting Regressor model. Then predicts a value based on this model.
	
	Parameters
	----------
	
	ListOfDicts : List
		List containing one or more dicts. These contain the data that will be used to train the model.
		
	ageGroup : String
		A string relating to an age group stored in the dict. This dictates what prices will be used to train, test and predict.
		
	dateToPredict : String
		A string in a date format Y-m-d. This is converted into an ordinal time format and then used as a input to predict the price with the trained model
	Returns
	-------
	**retruns** : String
		returns a string with the value predicted and the mean absolute error associated with the prediction.
	"""
	price = readInList(ListOfDicts, ageGroup)
	dateStr = readInList(ListOfDicts, "date")
	dateObj = []


	for i in dateStr:
		x = datetime.datetime.strptime(i[0], '%Y-%m-%d')
		x = [x.toordinal()]
		dateObj.append(x)
		
	priceAxis = price
	dateAxis = dateStr
	
	price = np.array(price).astype(np.float)
	dateObj = np.array(dateObj)
	
	datePred = datetime.datetime.strptime(dateToPredict, '%Y-%m-%d')
	datePred = [datePred.toordinal()]
	
	gb = GradientBoostingRegressor(n_estimators=200)
	gb.fit(dateObj, price)
	pred = gb.predict([datePred])
	
	priceAxis.append(pred[0])
	dateToPredict = [dateToPredict]
	dateAxis.append(dateToPredict)
	
	X_train, X_test, y_train, y_test = train_test_split(
	dateObj, price, train_size = 0.70
	)
	#predict values we already know
	y_pred = []

	for i in X_test:
		x = gb.predict([i])
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
	
	result = "Gradient Boosting = " + str(pred[0]) + " with Mean Absolute Error of " + str(error)
	createPredictionGraph(priceAxis, dateAxis)
	return(result)
