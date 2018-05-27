#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 19:19:27 2018

@author: eduardo
"""
import pandas as pd
import numpy as np
from math import *
import Harvesine
import sys
import time

df = pd.read_csv('new_york_hotels.csv', encoding='cp1252')

start = time.time()
df['distance'] = Harvesine.haversine(40.671, -73.985, df['latitude'].values, df['longitude'].values)

print(str(time.time() - start) + " seconds")