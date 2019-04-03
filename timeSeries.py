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

import datetime
import time

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from linearRegression import readInList

price = readInList(ListOfDicts, ageGroup)
dateStr = readInList(ListOfDicts, "date")
dateObj = []

	for i in dateStr:
		x = datetime.datetime.strptime(i[0], '%Y-%m-%d')
		dateObj.append(x)

data = pd.DataFrame({'date' : dateObj, 'price' : price})

y = data.price
y.index.name = 'time'
y.resample('Q', convention='start').asfreq()





