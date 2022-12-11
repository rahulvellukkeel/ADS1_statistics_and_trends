# -*- coding: utf-8 -*-
"""
@author: Rahul Mohanan Aikkatharayil
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_file(file_name):
    address = "E:/Herts/ADS1/Assignment 2/ADS1 Statistics and trends/" + file_name
    df = pd.read_excel(address)
    df_transpose = pd.DataFrame.transpose(df)
    return(df, df_transpose)

    
#df_pop_c,df_pop_t = read_file("Urban Population.xlsx.csv")
#df_co2_c,df_co2_t = ("CO2 Emmission.xlsx")

df_energy_total,df_energy_countries = read_file("Energy_Use.xls")
df_co2_total,df_co2_countries = read_file("CO2_Emission.xls")
df_renew_total,df_renew_countries = read_file("Renewable.xls")
df_gdp_total, df_gdp_countries =read_file("GDP_Per_Capita.xls")


"""
Energy used bar graph
"""
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

countries =['Canada', 'United Kingdom', 'China',  'France', 'India','United States', 'Bangladesh', 'Germany']
df_energy_time = pd.DataFrame.transpose(df_energy_countries)
years = [1990, 1995, 2000, 2005, 2010, 2014]
df_energy_subset_time = df_energy_time[years].copy()
df_energy_subset_time = df_energy_subset_time.loc[df_energy_subset_time.index.isin(countries)]

#print(df_energy_subset_time[1995])


n=8
r=np.arange(n)
width= 0.1
plt.bar(r-0.3, df_energy_subset_time[1990], color = 'grey',width = width, edgecolor = 'black',label='1990')
plt.bar(r-0.2, df_energy_subset_time[1995], color = 'g',width = width, edgecolor = 'black',label='1995')
plt.bar(r-0.1, df_energy_subset_time[2000], color = 'orange',width = width, edgecolor = 'black',label='2000')
plt.bar(r, df_energy_subset_time[2005], color = 'red',width = width, edgecolor = 'black',label='2005')
plt.bar(r+0.1, df_energy_subset_time[2010], color = 'steelblue',width = width, edgecolor = 'black',label='2010')
plt.bar(r+0.2, df_energy_subset_time[2014], color = 'black',width = width, edgecolor = 'black',label='2014')
plt.xlabel("Countries")
plt.ylabel("Energy use(kg of oil equivalent per capita)")
#plt.xticks(r+width/2,['1990','1995','2000','2005','2010'])
plt.legend()
plt.show()




df_energy_subset = df_energy_countries[countries].copy()
df_energy_subset = df_energy_subset.iloc[::5, :]
header_subset = df_energy_subset.iloc[0].values.tolist()
#print(df_energy_subset)

#df_energy_subset.to_excel("E:/Herts/ADS1/Assignment 2/ADS1 Statistics and trends/subset.xlsx")

"""
Co2 emission bar graph
"""

header = df_co2_countries.iloc[0].values.tolist()
df_co2_countries.columns = header


df_co2_countries = df_co2_countries.iloc[1:]
#print(df_energy_countries)
df_co2_countries = df_co2_countries.iloc[11:55]

df_co2_countries.index = df_co2_countries.index.astype(int)
df_co2_countries = df_co2_countries[df_co2_countries.index>1989]


#df_energy_total.to_excel("E:/Herts/ADS1/Assignment 2/ADS1 Statistics and trends/transposed2.xlsx")
df_co2_countries = df_co2_countries.dropna(axis = 'columns')
#df_energy_countries.to_excel("E:/Herts/ADS1/Assignment 2/ADS1 Statistics and trends/transposed.xlsx")

countries =['Canada', 'United Kingdom', 'China',  'France', 'India','United States', 'Bangladesh', 'Germany']
df_co2_time = pd.DataFrame.transpose(df_co2_countries)
years = [1990, 1995, 2000, 2005, 2010, 2014]
df_co2_subset_time = df_co2_time[years].copy()
df_co2_subset_time = df_co2_subset_time.loc[df_co2_subset_time.index.isin(countries)]

#print(df_energy_subset_time[1995])


n=8
r=np.arange(n)
width= 0.1
plt.bar(r-0.3, df_co2_subset_time[1990], color = 'aqua',width = width, edgecolor = 'black',label='1990')
plt.bar(r-0.2, df_co2_subset_time[1995], color = 'turquoise',width = width, edgecolor = 'black',label='1995')
plt.bar(r-0.1, df_co2_subset_time[2000], color = 'steelblue',width = width, edgecolor = 'black',label='2000')
plt.bar(r, df_co2_subset_time[2005], color = 'deepskyblue',width = width, edgecolor = 'black',label='2005')
plt.bar(r+0.1, df_co2_subset_time[2010], color = 'blue',width = width, edgecolor = 'black',label='2010')
plt.bar(r+0.2, df_co2_subset_time[2014], color = 'navy',width = width, edgecolor = 'black',label='2014')
plt.xlabel("Countries")
plt.ylabel("CO2 emissions (kt)")
#plt.xticks(r+width/2,['1990','1995','2000','2005','2010'])
plt.legend()
plt.show()




df_co2_subset = df_co2_countries[countries].copy()
df_co2_subset = df_co2_subset.iloc[::5, :]
header_subset = df_co2_subset.iloc[0].values.tolist()


"""
Renewable bar graph
"""


header = df_renew_countries.iloc[0].values.tolist()
df_renew_countries.columns = header


df_renew_countries = df_renew_countries.iloc[1:]
#print(df_energy_countries)
df_renew_countries = df_renew_countries.iloc[11:55]

df_renew_countries.index = df_renew_countries.index.astype(int)
df_renew_countries = df_renew_countries[df_renew_countries.index>1989]


#df_energy_total.to_excel("E:/Herts/ADS1/Assignment 2/ADS1 Statistics and trends/transposed2.xlsx")
df_renew_countries = df_renew_countries.dropna(axis = 'columns')
#df_energy_countries.to_excel("E:/Herts/ADS1/Assignment 2/ADS1 Statistics and trends/transposed.xlsx")

countries =['Canada', 'United Kingdom', 'China',  'France', 'India','United States', 'Bangladesh', 'Germany']
df_renew_time = pd.DataFrame.transpose(df_renew_countries)
years = [1990, 1995, 2000, 2005, 2010, 2014]
df_renew_subset_time = df_renew_time[years].copy()
df_renew_subset_time = df_renew_subset_time.loc[df_renew_subset_time.index.isin(countries)]

#print(df_energy_subset_time[1995])


n=8
r=np.arange(n)
width= 0.1
plt.bar(r-0.3, df_renew_subset_time[1990], color = 'aqua',width = width, edgecolor = 'black',label='1990')
plt.bar(r-0.2, df_renew_subset_time[1995], color = 'turquoise',width = width, edgecolor = 'black',label='1995')
plt.bar(r-0.1, df_renew_subset_time[2000], color = 'steelblue',width = width, edgecolor = 'black',label='2000')
plt.bar(r, df_renew_subset_time[2005], color = 'deepskyblue',width = width, edgecolor = 'black',label='2005')
plt.bar(r+0.1, df_renew_subset_time[2010], color = 'blue',width = width, edgecolor = 'black',label='2010')
plt.bar(r+0.2, df_renew_subset_time[2014], color = 'navy',width = width, edgecolor = 'black',label='2014')
plt.xlabel("Countries")
plt.ylabel("CO2 emissions (kt)")
#plt.xticks(r+width/2,['1990','1995','2000','2005','2010'])
plt.legend()
plt.show()




df_renew_subset = df_renew_countries[countries].copy()
df_renew_subset = df_renew_subset.iloc[::5, :]
header_subset = df_renew_subset.iloc[0].values.tolist()

"""
Lineplot
"""

header = df_gdp_countries.iloc[0].values.tolist()
df_gdp_countries.columns = header


df_gdp_countries = df_gdp_countries.iloc[1:]
#print(df_energy_countries)
df_gdp_countries = df_gdp_countries.iloc[11:55]

df_gdp_countries.index = df_gdp_countries.index.astype(int)
df_gdp_countries = df_gdp_countries[df_gdp_countries.index>1989]


#df_energy_total.to_excel("E:/Herts/ADS1/Assignment 2/ADS1 Statistics and trends/transposed2.xlsx")
df_gdp_countries = df_gdp_countries.dropna(axis = 'columns')

print(df_gdp_countries["India"])

plt.figure()
plt.plot(df_gdp_countries.index, df_gdp_countries["India"], '--')
plt.show()

