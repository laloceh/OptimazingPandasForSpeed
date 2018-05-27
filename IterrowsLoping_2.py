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

df = pd.read_csv('new_york_hotels.csv', encoding='cp1252')


# Haversine applied on rows via iteration
haversine_series = []

start = time.time()
for index, row in df.iterrows():
    haversine_series.append(Harvesine.haversine(40.671, -73.985, row['latitude'], row['longitude']))
df['distance'] = haversine_series

print(str(time.time() - start) + " seconds")