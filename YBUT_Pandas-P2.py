#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: YBUT_Pandas-P1.ipynb
Conversion Date: 2025-09-16T14:40:52.726Z
"""

# # **Programming Assignment 3**


# ## **Problem 2**


import pandas as pd # import the Pandas library with the 'pd'

cars = pd.read_csv ('cars.csv') # Read a CSV file into a pandas DataFrame
cars #print

# a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7 9 11)
cars.iloc[0:5, [1, 3, 5, 7, 9, 11]]  # Integer position-based selection of rows/columns using .iloc[...] and input odd number from 0-11

# b. Display the row that contains the 'Model' of 'Mazda RX4'
cars[cars['Model'] == 'Mazda RX4'] # filter DataFrame to show only the row with Model = 'Mazda RX4'

# c. How many cylinders ('cyl') does the car model 'Camaro Z28' have?
cars.loc[[23], ['Model', 'cyl']] # select row 23 and show only Model and cyl columns

# d. Determine how many cylinders ('cyl') and what gear type ('gear') do the car models 
# 'Mazda RX4 Wag', 'Ford Pantera L' and 'Honda Civic' have
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]