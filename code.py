# -*- coding: utf-8 -*-
"""
@author: Rahul Mohanan Aikkatharayil
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""
def read_file(file_name, df_name):
    address = "E:/Herts/ADS1/Assignment 2/Data/Power/" + file_name + ".csv"
    df_name = pd.read_csv(address)


    #return(df1,df2)
    return(df_name)

    
#df_pop_c,df_pop_t = read_file("Urban Population.xlsx.csv")
#df_co2_c,df_co2_t = ("CO2 Emmission.xlsx")


df_energy_total = read_file("API_EG.USE.PCAP.KG.OE_DS2_en_csv_v2_4697327", "df_energy_total")
print(df_energy_total)
"""

df_energy_total = pd.read_excel("E:/Herts/ADS1/Assignment 2/ADS1 Statistics and trends/Energy_Use.xls")

df_energy_countries = pd.DataFrame.transpose(df_energy_total)
header = df_energy_countries.iloc[0].values.tolist()
df_energy_countries.columns = header


df_energy_countries = df_energy_countries.iloc[1:]
#print(df_energy_countries)
df_energy_countries = df_energy_countries.iloc[11:55]

df_energy_countries.index = df_energy_countries.index.astype(int)
df_energy_countries = df_energy_countries[df_energy_countries.index>1989]

#print(df_energy_countries.index)
#df_energy_total.to_excel("E:/Herts/ADS1/Assignment 2/ADS1 Statistics and trends/transposed2.xlsx")
df_energy_countries = df_energy_countries.dropna(axis = 'columns')
#df_energy_countries.to_excel("E:/Herts/ADS1/Assignment 2/ADS1 Statistics and trends/transposed.xlsx")

countries =['Canada', 'United Kingdom', 'China', 'India', 'France', 'Brazil']
df_energy_time = pd.DataFrame.transpose(df_energy_countries)
years = [1990, 1995, 2000, 2005, 2010, 2014]
df_energy_subset_time = df_energy_time[years].copy()
df_energy_subset_time = df_energy_subset_time.loc[df_energy_subset_time.index.isin(countries)]

#print(df_energy_subset_time[1995])


n=6
r=np.arange(n)
width= 0.1
plt.bar(r-0.3, df_energy_subset_time[1990], color = 'b',width = width, edgecolor = 'black',label='1990')
plt.bar(r-0.2, df_energy_subset_time[1995], color = 'g',width = width, edgecolor = 'black',label='1995')
plt.bar(r-0.1, df_energy_subset_time[2000], color = 'orange',width = width, edgecolor = 'black',label='2000')
plt.bar(r, df_energy_subset_time[2005], color = 'red',width = width, edgecolor = 'black',label='2005')
plt.bar(r+0.1, df_energy_subset_time[2010], color = 'cyan',width = width, edgecolor = 'black',label='2010')
plt.bar(r+0.2, df_energy_subset_time[2014], color = 'black',width = width, edgecolor = 'black',label='2014')
plt.xlabel("Countries")
plt.ylabel(" Energy used")
#plt.xticks(r+width/2,['1990','1995','2000','2005','2010'])
plt.legend()
plt.show()




df_energy_subset = df_energy_countries[countries].copy()
df_energy_subset = df_energy_subset.iloc[::5, :]
header_subset = df_energy_subset.iloc[0].values.tolist()
#print(df_energy_subset)

#df_energy_subset.to_excel("E:/Herts/ADS1/Assignment 2/ADS1 Statistics and trends/subset.xlsx")



