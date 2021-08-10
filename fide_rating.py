#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:59:49 2021

@author: tddft
"""

import numpy as np
import matplotlib.pyplot as plt

file = open("standardrating.txt", "r")
file.readline()
Lines = file.readlines()

rating = np.zeros(len(Lines), dtype=int)
for index, element in enumerate(Lines):
    element_list = element.split()[-5:]
    
    try:
        rating[index] = int(element_list[0])
    
    except ValueError:
        rating[index] = int(element_list[1])

Lines = []
file.close()


hist, bin_edges = np.histogram(rating, bins=190, range=(1000., 2900.), density=True)
cumrating = 10*np.cumsum(hist)

plt.title('FIDE Ratings')
plt.plot(bin_edges[1:], len(rating)*hist)
plt.show()

plt.title('FIDE Cumlative Ratings')
plt.plot(bin_edges[1:], len(rating)*cumrating)
plt.show()

### GIVEN top X% GET rating
X = 1

def GetRating(percentile):
    percentile = (len(rating)*(1 - 0.01*percentile))
    absolute_val_array        = np.abs(len(rating)*cumrating - percentile)
    smallest_difference_index = absolute_val_array.argmin()
    return int(bin_edges[ smallest_difference_index ])

def GetPercentile(X_rating):
    absolute_val_array        = np.abs(bin_edges - X_rating)
    smallest_difference_index = absolute_val_array.argmin()
    
    return cumrating[ smallest_difference_index ]
     

percentile = (len(rating)*(1-0.01*X))
absolute_val_array = np.abs(len(rating)*cumrating - percentile)
smallest_difference_index = absolute_val_array.argmin()
print(int(bin_edges[smallest_difference_index]))

### GIVEN rating GET percentile
X_rating = 2380

absolute_val_array = np.abs(bin_edges - X_rating)
smallest_difference_index = absolute_val_array.argmin()
print((cumrating[smallest_difference_index]))





