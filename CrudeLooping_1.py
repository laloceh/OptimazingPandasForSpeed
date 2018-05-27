#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 18:47:32 2018

@author: eduardo
"""
import pandas as pd
import numpy as np
from math import *
import Harvesine
import sys
import time

# Define a function to manually loop over all rows and return a series of distances
def haversine_looping(df):
    distance_list = []
    for i in range(0, len(df)):
        d = Harvesine.haversine(40.671, -73.985, df.iloc[i]['latitude'], df.iloc[i]['longitude'])
        distance_list.append(d)
    return distance_list
    

df = pd.read_csv('new_york_hotels.csv', encoding='cp1252')

start = time.time()
# Run the haversine looping function
df['distance'] = haversine_looping(df)

print(str(time.time() - start) + " seconds")