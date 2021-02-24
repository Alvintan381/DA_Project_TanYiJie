#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: Tan Yi Jie, Alvin
#Group Name: ock
#Class: PN2004J
#Date: 2/9/2021
#Version: 1.0
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd

#Import matplotlib for pie chart
import matplotlib.pyplot as pit
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

  #Display sorted datafram for South East Asia Region within 1996 to 2006 
  print("The countries in the region are shown below.")
  print("Year range: 1996 - 2006" + "\n")

  #South East Asia Region on csv
  sea_region = df.iloc[216:348, 2:9]
  df1 = df.iloc[216:348, 0:2]
  result = df1.join(sea_region)

  #Print the total countries 
  print("Total number of the countries:", str(len(result.columns) - 2) + "\n")
  print(result)

  #Display the top 3 countries that visited Singapore over the span of 10 years 
  print("The Top 3 countries of visitors to Singapore from the selected region over the span of 10 years: ")

  print(df.iloc[216:348,2:9].sum(axis=0).sort_values(ascending=False).nlargest(3))

  return
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

  #read excel data 
  df = pd.read_csv('MonthyVisitors.csv')

  #All Regions
  Regions = ['South East Asia Region', 'Asia Pacific Region', 'South Asia Pacific Region', 'Middle East Region', 'Europe Region', 'North America Region', 'Australia Region', 'Africa Region']
  print('\n\n',Regions)

  #Region input for Error checking
  while True:
    x = 0
    #Display "Enter a Region user wish"
    Region = input("Please enter a region:")
    #If not in region, Display Error message
    if not Region in Regions:
      print("Error, Please try again!")

    elif Region in Regions:
      #South East Asia Region
      if Region == "South East Asia Region":
        sea_region = df.iloc[216:348, 2:9]
        x += 1
        break
      #Asia Pacific Region
      elif Region == "Asia Pacific Region":
        ap_region = df.iloc[216:348 ,9:14]
        x += 1
        break
      #South Asia Pacific Region
      elif Region == "South Asia Pacific Region":
        sap_region = df.iloc[216:348 ,14:17]
        x += 1
        break
      #Middle East Region
      elif Region == "Middle East Region":
        me_region = df.iloc[216:348 ,17:20]
        x += 1
        break
      #Europe Region
      elif Region == "Europe Region":
        eu_region = df.iloc[216:348 ,20:31]
        x += 1
        break
      #North America Region
      elif Region == "North America Region":
        na_region = df.iloc[216:348 ,31:33]
        x += 1
        break
      #Australia Region
      elif Region == "Australia Region":
        au_region = df.iloc[216:348 ,33:35]
        x += 1
        break
      #Africa Region
      elif Region == "Africa Region":
        af_region = df.iloc[216:348 ,35:36]
        x += 1
        break

  #List of years for error checking
  if x == 1:
    Years = ['1978-1984', '1985-1995', '1996-2006', '2007-2017']
    print('\n\n"',Years)

    while True:
      Year = input('\n\n' + "Select a year: ")
      try:
        Year = str(Year)
      except:
        #If not in years
        print("Invalid.")
      else:
        if Year in Years:
          if Year == '1978-1984' and Region == "South East Asia Region":
            year_range = df.iloc[0:85,0:2]
            country_df = df.iloc[0:85,2:9]
            total = year_range.join(country_df)
            print(total)
            x += 1
            break
          elif Year == '1985-1995':
            year_range = df.iloc[86:217, 0:2]
            country_df = df.iloc[86:217,2:9]
            total = year_range.join(country_df)
            print(total)
            x += 1
            break
          elif Year == '1996-2006':
            year_range = df.iloc[218:349, 0:2]
            country_df = df.iloc[218:349,2:9]
            total = year_range.join(country_df)
            print(total)
            x += 1
            break
          elif Year == '2007-2017':
            year_range = df.iloc[350:480, 0:2]
            country_df = df.iloc[350:480,2:9]
            total = year_range.join(country_df)
            print(total)
            x += 1
            break
        else:
          print("Invalid year!")

  #Pie Chart
  if x == 2:

    #South East Asia Region csv
    activities = ['Indonesia', 'Malaysia', 'Thailand', 'Philippines', 'Viet Nam', 'Brunei Darussalam', 'Myanmar' ]
    slices = [15288142, 6292852, 2961107, 2323026, 667954, 601772, 267938]
    colours = ['#5DADE2', '#9B59B6', '#F4D03F', '#F39C12', '#ECF0F1', '#C0392B', '#566573']

    #Pie Chart for South East Asia Region
    pit.pie(slices,
        labels=activities,
        startangle=90,
        shadow=True,
        explode=(0.3, 0, 0, 0, 0, 0, 0),
        autopct='%1.2f%%')

    #Show Pie Chart
    pit.show()


#########################################################################
#Main Branch: End of Code
#########################################################################