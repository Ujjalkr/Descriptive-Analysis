# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:18:06 2020

@author: iamuj
"""


#from tabulate import tabulate
import csv   #import csv for creating a csv file
import math   #importing math , for computing math function
from math import sin, cos, sqrt
from math import pi   
b=86; l=150; a=50     # all these quantities are given

with open('amar01.csv','w', newline='') as file:   # is part of creating csv file
    writer=csv.writer(file)
    writer.writerow(['Theta','Volume' ,'S'])
    for t in range(361):     # here range(360 meana 0 to 360 degree  with interval of 1 degree
        
        
        theta=t*pi/180
    
        s=(a*cos(theta)+sqrt(pow(l,2)-pow(a,2)*pow(sin(theta),2)))
        V=((math.pi*pow(b,2))/4)*(l+a-s)
        writer.writerow([t, V,s])
   
   
import pandas as pd   #importing pandas fo readig csv file which we created
datas=pd.read_csv("amar01.csv")   #amar01.csv is our csv file
#x=datas.iloc[:, -2]
#y=datas.iloc[:, -1]
x=datas['Theta']     #Assign theta's with x     
y=datas['Volume']    #Assign volume with y


import matplotlib.pyplot as plt     #importing  for plor
import numpy as np

fig=plt.figure(figsize=(15,8))
plt.plot(x,y,'r--')             #plot, 
plt.xlabel("Theta in Degree")    #X axis  label
plt.ylabel("Volume in mm3")      #Y axis label
plt.title("Variation of Volume with crank angle")   # Title of the plot

#plt.plot(x,y,'r--')
#plt.axhline(y=50000,color='gray',linestyle='--')    # If Vc is given
plt.axvline(x=180,color='grey',linestyle='--')
#plt.figure(figsize=(3,4)) 
#plt.title("Variation of volume with crank angle by Ujjal")
#plt.xlabel("theta in degree")
#plt.ylabel("Volume in mm3")

plt.xticks(np.arange(0, 360, 15))
plt.yticks(np.arange(0, 600000, 50000))
#plt.grid()
plt.grid(color='b', ls = '-.', lw = 0.25)
plt.show()
