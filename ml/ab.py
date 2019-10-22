# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:19:13 2019

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cars_data=pd.read_csv('Toyota.csv',index_col=0,na_values=["??"])
print(cars_data)
cars_data.dropna(axis=0,inplace=True)
print(cars_data)

plt.scatter(cars_data['Age'],cars_data['Price'],c='grey')
plt.title('scatter plot of PRICE vs AGE OF CARS')
plt.xlabel('Age:(Months)')
plt.ylabel('Price:(Dollars)')
plt.show()
plt.savefig("scatter .png")
plt.hist(cars_data['KM'],color='green',edgecolor='white',bins=9)
plt.title('Histogram of kilometer')
plt.xlabel('Kilometer:(km)')
plt.ylabel('Frequency')
plt.show()


counts=[979,120,12]
fuelType=['petrol','diesel','CNG']
index=np.arange(len(fuelType))

plt.bar(index,counts,color=['red','blue','cyan'])
plt.title('Bar plts of fuel types')
plt.xlabel('Fuel Type')
plt.ylabel('Frequency')
plt.show()


plt.bar(index,counts,color=['red','blue','cyan'])
plt.title('Bar plts of fuel types')
plt.xlabel('Fuel Type')
plt.ylabel('Frequency')
plt.xticks(index,fuelType)
plt.show()
