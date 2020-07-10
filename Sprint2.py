# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:55:14 2020

@author: Dewald
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ilist1 = ['Simba','Coke','Cadbury','Pepper Steak','Pear','Vanilla','Spinach']
ilist2 = ['Lays','Fanta','Tex','Chicken','Apple','Chocolate','Cabbage']
ilist3 = ['','','','','Orange','','']

df = pd.DataFrame([(ilist1),
                    (ilist2),
                    (ilist3)],
                  index=['1','2','3'],
                  columns=('Chips', 'Cooldrinks','Chocolates','Pies','Fruit','Cupcakes','Veggies'))

Plots = np.genfromtxt("Plotstonks.csv", delimiter = ",", names = ["Item", "Chips", "Cooldrinks", "Chocolates", "Pies", "Fruit", "Cupcakes", "Veggies"])

plt.xlabel('Months')
plt.ylabel('Stonks(Stock level)') 

plt.plot(Plots["Chips"] ,label = "Chips")
plt.plot(Plots["Cooldrinks"],label = "Cooldrinks") 
plt.plot(Plots["Chocolates"],label = "Chocolates")
plt.plot(Plots["Pies"],label = "Pies")
plt.plot(Plots["Fruit"],label = "Fruit")
plt.plot(Plots["Cupcakes"],label = "Cupcakes")
plt.plot(Plots["Veggies"],label = "Veggies")
plt.legend(loc = "upper right")
