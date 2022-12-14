# -*- coding: utf-8 -*-
"""
@author: Rahul Mohanan Aikkatharayil
"""

#importing requiredpackages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_file(file_name):
    """
        This function takes name of the file and reads the file from local directory and loads it into a dataframe.
        It then transposes the dataframe and returns both the first and transposed dataframes
    """

    address = "E:/Herts/ADS1/Assignment 2/ADS1 Statistics and trends/" + file_name
    df = pd.read_excel(address)
    df_transpose = pd.DataFrame.transpose(df)
    return(df, df_transpose)

#Reads the files
df_energy_total,df_energy_countries = read_file("Electric_power_consumption.xls")
df_co2_total,df_co2_countries = read_file("CO2_Emission.xls")
df_renew_total,df_renew_countries = read_file("Renewable.xls")
df_gdp_total, df_gdp_countries = read_file("GDP_Per_Capita.xls")





"""
Electric power used bar graph
Creating bar graph of energy used by mutiple countries from 1990-2014
"""

#Header setting
header = df_energy_countries.iloc[0].values.tolist()
df_energy_countries.columns = header

#Cleaning the dataframe
df_energy_countries = df_energy_countries.iloc[1:]
df_energy_countries = df_energy_countries.iloc[11:55]

#Converting index ot int
df_energy_countries.index = df_energy_countries.index.astype(int)
df_energy_countries = df_energy_countries[df_energy_countries.index>1989]
df_energy_countries = df_energy_countries.dropna(axis = 'columns')

#Creates a list of countries to use in the plot
#countries =['Bangladesh', 'Kenya', 'United Kingdom', 'China',  'France', 'India','United States', 'Germany', 'Saudi Arabia']
countries =['Bangladesh', 'China', 'Germany', 'France',  'United Kingdom', 'India','Kenya', 'Saudi Arabia', 'United States']
countries_label =['BD', 'CN', 'DE',  'FR', 'UK', 'IN', 'KE', 'KSA', 'US']
df_energy_time = pd.DataFrame.transpose(df_energy_countries)
years = [1990, 1994, 1998, 2002, 2006, 2010, 2014]

#selecting only required data
df_energy_subset_time = df_energy_time[years].copy()
df_energy_subset_time = df_energy_subset_time.loc[df_energy_subset_time.index.isin(countries)]

#plotting the data
n=9
r=np.arange(n)
width= 0.1
plt.bar(r-0.3, df_energy_subset_time[1990], color = 'grey',width = width, edgecolor = 'black',label='1990')
plt.bar(r-0.2, df_energy_subset_time[1994], color = 'g',width = width, edgecolor = 'black',label='1994')
plt.bar(r-0.1, df_energy_subset_time[1998], color = 'orange',width = width, edgecolor = 'black',label='1998')
plt.bar(r, df_energy_subset_time[2002], color = 'red',width = width, edgecolor = 'black',label='2002')
plt.bar(r+0.1, df_energy_subset_time[2006], color = 'steelblue',width = width, edgecolor = 'black',label='2006')
plt.bar(r+0.2, df_energy_subset_time[2010], color = 'greenyellow',width = width, edgecolor = 'black',label='2010')
plt.bar(r+0.3, df_energy_subset_time[2014], color = 'khaki',width = width, edgecolor = 'black',label='2014')
plt.xlabel("Countries")
plt.ylabel("Energy use")
plt.xticks(width+r, countries_label)
plt.legend()
plt.title("Energy use (kg of oil equivalent per capita)")
plt.savefig("line1.png", dpi=300, bbox_inches='tight')
#plt.savefig("Energy_use.png", dpi=300, bbox_inches='tight')
plt.show()



"""
Co2 emission bar graph
Creating bar graph of Co2 emission of multiple countries from 1990-2014
"""

header = df_co2_countries.iloc[0].values.tolist()
df_co2_countries.columns = header

#Cleaning the dataframe

df_co2_countries = df_co2_countries.iloc[1:]
df_co2_countries = df_co2_countries.iloc[11:55]

df_co2_countries.index = df_co2_countries.index.astype(int)
df_co2_countries = df_co2_countries[df_co2_countries.index>1989]

df_co2_countries = df_co2_countries.dropna(axis = 'columns')

df_co2_time = pd.DataFrame.transpose(df_co2_countries)

df_co2_subset_time = df_co2_time[years].copy()
df_co2_subset_time = df_co2_subset_time.loc[df_co2_subset_time.index.isin(countries)]

#plotting the data
plt.bar(r-0.3, df_co2_subset_time[1990], color = 'aqua',width = width, edgecolor = 'black',label='1990')
plt.bar(r-0.2, df_co2_subset_time[1994], color = 'turquoise',width = width, edgecolor = 'black',label='1995')
plt.bar(r-0.1, df_co2_subset_time[1998], color = 'steelblue',width = width, edgecolor = 'black',label='2000')
plt.bar(r, df_co2_subset_time[2002], color = 'deepskyblue',width = width, edgecolor = 'black',label='2005')
plt.bar(r+0.1, df_co2_subset_time[2006], color = 'blue',width = width, edgecolor = 'black',label='2010')
plt.bar(r+0.2, df_co2_subset_time[2010], color = 'navy',width = width, edgecolor = 'black',label='2014')
plt.bar(r+0.3, df_co2_subset_time[2014], color = 'darkgrey',width = width, edgecolor = 'black',label='2014')
plt.xlabel("Countries")
plt.ylabel("CO2 emission")
plt.xticks(width+r, countries_label)
plt.legend()
plt.title("CO2 emissions (kt)")
#plt.savefig("Co2.png", dpi=300, bbox_inches='tight')
plt.show()



"""
Renewable bar graph
Creates a bar chart of renewale energy consumption of multiple countries during 1990-2014
"""


header = df_renew_countries.iloc[0].values.tolist()
df_renew_countries.columns = header

#Cleaning the dataframe

df_renew_countries = df_renew_countries.iloc[1:]
df_renew_countries = df_renew_countries.iloc[11:55]

df_renew_countries.index = df_renew_countries.index.astype(int)
df_renew_countries = df_renew_countries[df_renew_countries.index>1989]

df_renew_countries = df_renew_countries.dropna(axis = 'columns')

df_renew_time = pd.DataFrame.transpose(df_renew_countries)
df_renew_subset_time = df_renew_time[years].copy()
df_renew_subset_time = df_renew_subset_time.loc[df_renew_subset_time.index.isin(countries)]

#print(df_energy_subset_time[1995])

#plotting the data
plt.bar(r-0.3, df_renew_subset_time[1990], color = 'pink',width = width, edgecolor = 'black',label='1990')
plt.bar(r-0.2, df_renew_subset_time[1994], color = 'deeppink',width = width, edgecolor = 'black',label='1995')
plt.bar(r-0.1, df_renew_subset_time[1998], color = 'coral',width = width, edgecolor = 'black',label='2000')
plt.bar(r, df_renew_subset_time[2002], color = 'khaki',width = width, edgecolor = 'black',label='2005')
plt.bar(r+0.1, df_renew_subset_time[2006], color = 'yellow',width = width, edgecolor = 'black',label='2010')
plt.bar(r+0.2, df_renew_subset_time[2010], color = 'greenyellow',width = width, edgecolor = 'black',label='2014')
plt.bar(r+0.3, df_renew_subset_time[2014], color = 'green',width = width, edgecolor = 'black',label='2014')
plt.xlabel("Countries")
plt.ylabel("Energy(Renewable)")
plt.xticks(width+r, countries_label)
plt.legend()
plt.title("Renewable energy consumption (% of total final energy consumption)")
#plt.savefig("Renewable.png", dpi=300, bbox_inches='tight')
plt.show()


"""
Lineplot gdp per capita
Creates a lineplot of GDP Per capita of multiple countries during 1990-2014.
Used mean to fill empty cells
"""

header = df_gdp_countries.iloc[0].values.tolist()
df_gdp_countries.columns = header

#Cleaning the dataframe
df_gdp_countries = df_gdp_countries.iloc[1:]
df_gdp_countries = df_gdp_countries.iloc[11:55]

df_gdp_countries.index = df_gdp_countries.index.astype(int)
df_gdp_countries = df_gdp_countries[df_gdp_countries.index>1990]

#using mean() function of pandas to fill empty cells of Israel
df_gdp_countries["Israel"] = df_gdp_countries["Israel"].interpolate(method='nearest', axis=0).ffill().bfill()


#plotting the data
plt.figure()
plt.plot(df_gdp_countries.index, df_gdp_countries["Bangladesh"])
plt.plot(df_gdp_countries.index, df_gdp_countries["China"] )
plt.plot(df_gdp_countries.index, df_gdp_countries["Germany"])
plt.plot(df_gdp_countries.index, df_gdp_countries["France"])
plt.plot(df_gdp_countries.index, df_gdp_countries["United Kingdom"])
plt.plot(df_gdp_countries.index, df_gdp_countries["India"])
plt.plot(df_gdp_countries.index, df_gdp_countries["Kenya"])
plt.plot(df_gdp_countries.index, df_gdp_countries["Saudi Arabia"])
plt.plot(df_gdp_countries.index, df_gdp_countries["United States"])
plt.plot(df_gdp_countries.index, df_gdp_countries["Israel"])
plt.xlim(1991,2014)
plt.xlabel("Year")
plt.ylabel("GDP")
plt.legend(['BD', 'CN', 'DE',  'FR', 'UK', 'IN', 'KE', 'KSA', 'US', 'IL'], prop = {'size': 8})
plt.title("GDP per capita, PPP (current international $)")
#plt.savefig("GDP Per Capita.png", dpi = 300, bbox_inches='tight')
plt.show()

