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
	
	y_pred = svr.predict([datePred])
	
	print("SVM++++++++++++++")
	print(y_pred)
	return(y_pred)

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
	y_pred_rf = clf_rf.predict([datePred])
	
	print(y_pred_rf)
	return(y_pred_rf)
