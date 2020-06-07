# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:40:13 2020

@author: aortegar
"""

import numpy as py
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\aortegar\Desktop\data.csv",sep=";")
df

class CostFunction:
    
    def __init__(self,dataset,varObj):
        self.dataset = dataset
        self.varObj = varObj
    
    def plotData(self,x):
        #x es el nombre de la columna que se va a representar contra y
        xValues = self.dataset[x].tolist()
        yValues = self.dataset[self.varObj].tolist()
        
        plt.plot(xValues, yValues, 'ro')
        plt.axis([min(xValues),max(xValues),min(yValues),max(yValues)])
        plt.show()    
    