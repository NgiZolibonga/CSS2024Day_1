# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:13:59 2024

@author: Ngizolibonga
"""

import pandas

file = pandas.read_csv("country_data.csv")
print(file)
print(file.info())
print(file.describe())

import pandas
file = pandas.read_csv("diab_data.csv")
print(file)
print(file.info())
print(file.describe())

file = pandas.read_csv("insurance_data.csv",skiprows=5)
print(file)
print(file.info())
print(file.describe())

file = pandas.read_csv("iris.csv")
print(file)
print(file.info())
print(file.describe())

