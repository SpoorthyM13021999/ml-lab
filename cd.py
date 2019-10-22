# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:56:43 2019

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cars_data=pd.read_csv('Toyota.csv',index_col=0,na_values=["??"])
print(cars_data)
cars_data.dropna(axis=0,inplace=True)


sns.set(style="darkgrid")
sns.regplot(x=cars_data['Age'],y=cars_data['Price'],fit_reg=False,marker="^")
sns.lmplot(x='Age',y='Price',data=cars_data,fit_reg=False,hue='FuelType',legend=True,palette='Set2')
#print(cars_data)