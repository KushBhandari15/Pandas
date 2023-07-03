# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:35:14 2022

@author: Kush Bhandari
"""

import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
from pandas import DataFrame, Series 

sh_raw =  pd.read_csv('/Users/Kush Bhandari/Desktop/movies.csv',  header=None,            
 names= ['Year','Title','Comic','IMDB','RT', 'CompositeRating','OpeningWeekendBoxOffice',
'AvgTicketPriceThatYear','EstdOpeningAttendance','USPopThatYear']) 
#print(sh_raw.head(5))

sh = sh_raw[np.isfinite(sh_raw.OpeningWeekendBoxOffice)] 
#print(sh.head(5)) 

imdb_normalized = sh.IMDB / 10    
         
sh.insert(10,'IMDBNormalized',imdb_normalized) 
rt_normalized = sh.RT/100         
     
sh.insert(11, 'RTNormalized', rt_normalized)
sh.plot.scatter(x ='RTNormalized',y ='IMDBNormalized') 
plt.show()

#print(sh[['RTNormalized','IMDBNormalized']].corr()) 

#print(sh[['RTNormalized','IMDBNormalized']].describe())

#TASK 1
print('TASK 1')
print('\n\n')
print(sh[sh["Comic"]=='DC'])

print('\n\n')
print('TASK 2')
print('\n\n')
#TASK 2
print(sh[['Year','Title','OpeningWeekendBoxOffice']])

print('\n\n')
#Task 3
print('\n\n')
print('TASK 3')
sh_temp=sh[sh["Comic"]=='Marvel']
print(sh_temp[['Year','Title']])

print('\n\n')
#TASK 4
print('\n\n')
print('TASK 4')
y=sh['AvgTicketPriceThatYear']
x=sh['Year']
plt.plot(x,y)
plt.show()


