#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: Tan Yi Jie, Alvin
#Group Name: OCK
#Class: PN2004J
#Date: 2/9/2021
#Version: 1.0
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd

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

	#Display sorted dataframe for South East Asia Region Within 1996 to 2006
	print("\n\n" + "South-East-Asia region was selected.")

	#Display sorted dataframe based on given year range of region (1996-2006)
	print("The countries in the region are shown below.")
	print(" Year range: 1996 - 2006" + "\n")
	sea_region = df.iloc[216:348, 2:9]
	df1 = df.iloc[216:347, 0:2]
	result = df1.join(sea_region)
	print("Total number of the countries:", str(len(result.columns) - 2) + "\n")
	print(result)

	#Display the top 3 countries that visited Singapore over the span of 10 years
	print(
	    "\n" +
	    "The Top 3 countries of visitors to Singapore from the selected region over the span of 10 years:"
	)
	print(df.iloc[216:348,
	              2:9].sum(axis=0).sort_values(ascending=False).nlargest(3))              

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

import matplotlib.pyplot as pit

activities = ['Indonesia', 'Malaysia', 'Thailand', 'Philippines', 'Viet Nam', 'Brunei Darussalam', 'Myanmar'  ]
slices = [15288142, 6292852, 2961107, 2323026, 667954, 601772, 267938]
colours = ['#5DADE2', '#9B59B6', '#F4D03F', '#F39C12', '#ECF0F1', '#C0392B', '#566573' ]

#Pie chart
pit.pie(slices,
        labels=activities,
        startangle=90,
        shadow=True,
        colors=colours,
        explode=(0.3, 0, 0, 0, 0, 0, 0),
        autopct='%1.2f%%')

#Show legend
pit.legend()

#Show pie chart
pit.show()

#########################################################################
#Main Branch: End of Code
#########################################################################
