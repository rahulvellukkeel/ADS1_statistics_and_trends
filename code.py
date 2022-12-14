# -*- coding: utf-8 -*-
"""
@author: Rahul Mohanan Aikkatharayil
"""

#importing requiredpackages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


def read_file(file_name):
    """
    This function takes name of the file and reads it from local directory and loads it into a dataframe.
    Then transposes the dataframe and returns both the first and transposed dataframes. It also sets
    the header for the transposed dataframe

    Parameters
    ----------
    file_name : string
        Name of the file tobe read into the datarame.

    Returns
    -------
    A dataframe loaded from the file and it's transpose.

    """

    address = "E:/Herts/ADS1/Assignment 2/ADS1 Statistics and trends/" + file_name
    df = pd.read_excel(address)
    df_transpose = pd.DataFrame.transpose(df)
    #Header setting
    header = df_transpose.iloc[0].values.tolist()
    df_transpose.columns = header
    return(df, df_transpose)


def clean_df(df):
    """
    

    Parameters
    ----------
    df : dataframe
        Dataframe that needs to be cleaned and index converted.

    Returns
    -------
    df : dataframe
        dataframe with required columns and index as int.

    """

    #Cleaning the dataframe
    df = df.iloc[1:]
    df = df.iloc[11:55]
    
    #Converting index ot int
    df.index = df.index.astype(int)
    df = df[df.index>1989]

    #cleaning empty cells
    df = df.dropna(axis = 'columns')
    return df


def country_df(country_name):
    """
    Creates a dataframe for the country with electricity usage, co2 emission, gdp, renewable energy as columns

    Parameters
    ----------
    country_name : string
        Name of the country to create the dataframe.

    Returns
    -------
    df_name : dataframe
        Newly created dataframe.

    """

    #creates dataframe name
    df_name = "df_" + country_name
    #creates dataframe
    df_name = pd.concat([df_energy_countries[country_name].astype(float), df_pop_countries[country_name].astype(float), df_gdp_countries[country_name].astype(float), df_renew_countries[country_name].astype(float), df_co2_countries[country_name].astype(float)], axis =1)
    #Gives column names
    df_name.columns.values[0] = "Electricity"
    df_name.columns.values[1] = "Population"
    df_name.columns.values[2] = "GDP"
    df_name.columns.values[3] = "Renewable"
    df_name["GDP"] = df_name["GDP"].interpolate(method='linear', axis=0).ffill().bfill()
    df_name.columns.values[4] = "CO2"
    return (df_name)


def heatmap(country_name):
    """
    Creates a correlation heatmap for the country given as argument.

    Parameters
    ----------
    country_name : string
        Name of the country to create the heatmap for.

    Returns
    -------
    None.

    """

    #creates dataframe name
    df_name = "df_" + country_name
    #cals function to create dataframe
    df_name = country_df(country_name)
    #plots heatmap
    dataplot = sb.heatmap(df_name.corr(), cmap="YlGnBu", annot=True)
    #saves figure
    filename = country_name + "_heatmap.png"
    plt.savefig(filename, dpi = 300, bbox_inches='tight')
    plt.show()


#Reads the files
df_energy_total,df_energy_countries = read_file("Electric_power_consumption.xls")
df_co2_total,df_co2_countries = read_file("CO2_Emission.xls")
df_renew_total,df_renew_countries = read_file("Renewable.xls")
df_gdp_total, df_gdp_countries = read_file("GDP_Per_Capita.xls")
df_pop_total, df_pop_countries = read_file("Population_total.xls")



#Creates a list of countries and years to use in the plots
countries =['Bangladesh', 'China', 'Germany', 'France',  'United Kingdom', 'India','Kenya', 'Saudi Arabia', 'United States']
countries_label =['BD', 'CN', 'DE',  'FR', 'UK', 'IN', 'KE', 'KSA', 'US']
years = [1990, 1994, 1998, 2002, 2006, 2010, 2014]


"""
Electric power used bar graph
Creating bar graph of Electric power consumption (kWh per capita) by mutiple countries from 1990-2014
"""

#Cleaning the dataframe
df_energy_countries = clean_df(df_energy_countries)

#selecting only required data
df_energy_time = pd.DataFrame.transpose(df_energy_countries)
df_energy_subset_time = df_energy_time[years].copy()
df_energy_subset_time = df_energy_subset_time.loc[df_energy_subset_time.index.isin(countries)]

#plotting the data
n= len(countries)
r=np.arange(n)
width= 0.1
plt.bar(r-0.3, df_energy_subset_time[1990], color = 'grey',width = width, edgecolor = 'black',label='1990')
plt.bar(r-0.2, df_energy_subset_time[1994], color = 'green',width = width, edgecolor = 'black',label='1994')
plt.bar(r-0.1, df_energy_subset_time[1998], color = 'orange',width = width, edgecolor = 'black',label='1998')
plt.bar(r, df_energy_subset_time[2002], color = 'red',width = width, edgecolor = 'black',label='2002')
plt.bar(r+0.1, df_energy_subset_time[2006], color = 'steelblue',width = width, edgecolor = 'black',label='2006')
plt.bar(r+0.2, df_energy_subset_time[2010], color = 'greenyellow',width = width, edgecolor = 'black',label='2010')
plt.bar(r+0.3, df_energy_subset_time[2014], color = 'khaki',width = width, edgecolor = 'black',label='2014')
plt.xlabel("Countries")
plt.ylabel("Electricity use")
plt.xticks(width+r, countries_label)
plt.legend()
plt.title("Electric power consumption (kWh per capita)")
plt.savefig("Electric_power.png", dpi=300, bbox_inches='tight')
plt.show()



"""
Co2 emission bar graph
Creating bar graph of CO2 emissions (kt) of multiple countries from 1990-2014
"""

#Cleaning the dataframe
df_co2_countries = clean_df(df_co2_countries)

#selecting only required data
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
plt.savefig("Co2.png", dpi=300, bbox_inches='tight')
plt.show()



"""
Renewable bar graph
Creates a bar chart of Renewable energy consumption (% of total final energy consumption)
of multiple countries during 1990-2014
"""

#Cleaning the dataframe
df_renew_countries = clean_df(df_renew_countries)
#selecting only required data
df_renew_time = pd.DataFrame.transpose(df_renew_countries)
df_renew_subset_time = df_renew_time[years].copy()
df_renew_subset_time = df_renew_subset_time.loc[df_renew_subset_time.index.isin(countries)]


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
plt.savefig("Renewable.png", dpi=300, bbox_inches='tight')
plt.show()


"""
Lineplot gdp per capita
Creates a lineplot of GDP Per capita of multiple countries during 1990-2014.
Used mean to fill empty cells of Israel
"""


#Cleaning the dataframe
#Clean function is not used here because it will remove entirety of Israel column
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
plt.savefig("GDP_Per_Capita.png", dpi = 300, bbox_inches='tight')
plt.show()



"""
Lineplot total population
Creates a lineplot of total population of multiple countries during 1990-2014.
"""
#Cleaning the dataframe
#Clean function is not used here because it will remove entirety of Israel column
df_pop_countries = df_pop_countries.iloc[1:]
df_pop_countries = df_pop_countries.iloc[11:55]

df_pop_countries.index = df_pop_countries.index.astype(int)
df_pop_countries = df_pop_countries[df_pop_countries.index>1990]


#using mean() function of pandas to fill empty cells of Israel
df_pop_countries["Israel"] = df_pop_countries["Israel"].interpolate(method='nearest', axis=0).ffill().bfill()


#plotting the data
plt.figure()
plt.plot(df_pop_countries.index, df_pop_countries["Bangladesh"])
plt.plot(df_pop_countries.index, df_pop_countries["China"] )
plt.plot(df_pop_countries.index, df_pop_countries["Germany"])
plt.plot(df_pop_countries.index, df_pop_countries["France"])
plt.plot(df_pop_countries.index, df_pop_countries["United Kingdom"])
plt.plot(df_pop_countries.index, df_pop_countries["India"])
plt.plot(df_pop_countries.index, df_pop_countries["Kenya"])
plt.plot(df_pop_countries.index, df_pop_countries["Saudi Arabia"])
plt.plot(df_pop_countries.index, df_pop_countries["United States"])
plt.plot(df_pop_countries.index, df_pop_countries["Israel"])
plt.xlim(1991,2014)
plt.xlabel("Year")
plt.ylabel("Population")
plt.legend(['BD', 'CN', 'DE',  'FR', 'UK', 'IN', 'KE', 'KSA', 'US', 'IL'], prop = {'size': 8})
plt.title("Population, total")
plt.savefig("Population.png", dpi = 300, bbox_inches='tight')
plt.show()


"""
Calls the functions to create the heatmaps
"""

heatmap("China")
heatmap("United Kingdom")
heatmap("France")



