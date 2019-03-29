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
import matplotlib.pyplot as plt
import datetime

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


	#plt.scatter(dateObj,price,color='black')
	#predicted_values = [reg.coef_ * i + reg.intercept_ for i in dateObj]
	#plt.plot(dateObj, predicted_values, 'b')
	#plt.xlabel("monthly admissions")
	#plt.ylabel("price")
	#plt.show()

	datePred = datetime.datetime.strptime("2017-07-01", '%Y-%m-%d')
	datePred = [datePred.toordinal()]

	test = reg.predict(X=[datePred])
	print(test[0])
