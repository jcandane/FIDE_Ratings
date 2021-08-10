#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:59:49 2021
@author: julio candanedo
"""

import numpy as np
import matplotlib.pyplot as plt
import requests ## install requests
import os 
import zipfile

# =============================================================================
# Input
# =============================================================================

YEAR  = "2021"
MONTH = "Aug"
TYPE  = "Standard" ## "rapid" "blitz"

# =============================================================================
# Code
# =============================================================================

### download ZIP file
url = "http://ratings.fide.com/download/" + TYPE.lower() + "_" + MONTH.lower() + YEAR[2:] + "frl.zip" # "http://ratings.fide.com/download/standard_aug21frl.zip"
req = requests.get(url)
filename = req.url[url.rfind("/")+1:]

with open(filename, "wb") as f:
    for chunk in req.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

### UNZIP file -> Get .TXT file
file_path = os.getcwd() + "/" +  req.url[url.rfind("/")+1:]
with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall(os.getcwd() )


### Real .TXT file -> Get Data
file = open(req.url[url.rfind("/")+1:-4] + ".txt", "r")
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

def GetRating(percentile):
    ### GIVEN top X% GET rating
    percentile = (len(rating)*(1 - 0.01*percentile))
    absolute_val_array        = np.abs(len(rating)*cumrating - percentile)
    smallest_difference_index = absolute_val_array.argmin()
    return int(bin_edges[ smallest_difference_index ])

def GetPercentile(X_rating):
    ### GIVEN rating GET percentile
    absolute_val_array        = np.abs(bin_edges - X_rating)
    smallest_difference_index = absolute_val_array.argmin()
    
    return cumrating[ smallest_difference_index ]

# =============================================================================
# Plot Data
# =============================================================================

hist, bin_edges = np.histogram(rating, bins=1900, range=(1000., 2900.), density=True)
cumrating = 1*np.cumsum(hist)

Name = TYPE + "_" + MONTH + "_" + YEAR
plt.title( TYPE + " " + MONTH + ". " + YEAR + " FIDE Ratings" )
plt.plot(bin_edges[1:], len(rating)*hist)
plt.xlabel("Rating")
plt.ylabel("Number of Players with Rating")
plt.savefig(Name + "_ratings.png", dpi=200)
plt.show()

plt.title( TYPE + " " + MONTH + ". " + YEAR + " FIDE Cumulative Ratings" )
plt.plot(bin_edges[1:], len(rating)*cumrating)
plt.plot( GetRating(0.1)*np.ones(50), np.linspace(0, 1.05*len(rating), 50), linestyle="dashed", label="top 0.1 Percentile")
plt.plot( GetRating(2.0)*np.ones(50), np.linspace(0, 1.05*len(rating), 50), linestyle="dashed", label="top 2 Percentile")
plt.plot( GetRating(16.)*np.ones(50), np.linspace(0, 1.05*len(rating), 50), linestyle="dashed", label="top 16 Percentile")
plt.plot( GetRating(50.)*np.ones(50), np.linspace(0, 1.05*len(rating), 50), linestyle="dashed", label="50 Percentile")
plt.plot( GetRating(84.)*np.ones(50), np.linspace(0, 1.05*len(rating), 50), linestyle="dashed", label="bottom 16 Percentile")
plt.xlabel("Rating")
plt.ylabel("Players")
plt.legend()
plt.savefig(Name + "_cumulativeratings.png", dpi=200)
plt.show()

print( GetPercentile(GetRating(1)) )