#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  linearRegression.py
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
from sklearn import linear_model
import datetime
from graph import createPredictionGraph
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def readInList(ListOfDicts, ageGroup):
	price = []
	date = []
	data = dict()
	for row in range(0,len(ListOfDicts)):
		query_data = ListOfDicts[row]
		y = [query_data[ageGroup] ]
		price.append(y)

	return price

def linearReg(ListOfDicts, ageGroup, dateToPredict):
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
