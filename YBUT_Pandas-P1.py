#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: YBUT_Pandas-P2 (2) (1).ipynb
Conversion Date: 2025-09-16T14:49:10.548Z
"""

# # **Programming Assignment 3**


# ## **Problem 1**


import pandas as pd # import the Pandas library with the 'pd'

cars = pd.read_csv ('cars.csv') # Read a CSV file into a pandas DataFrame
cars #print

cars.head (5) # print the first 5 rows

cars.tail (5) # print the last 5 rows