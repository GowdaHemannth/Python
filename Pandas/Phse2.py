import pandas as pd
import numpy as np

## Here we will Learn About Viewing the Data 
data = pd.read_csv("Pandas/nba.csv")


print("The first 5 rows of the Data ")
print(data.head())
## You can retrive as Many Data from these Using n=7 inside Head Operations     
## For particular Column or a row 
D=data['Salary']
print(D.head)

## You can sort the Values from the Data 
sorted_Data=data.sort_values(by='Age',ascending=True)
Sort=sorted_Data.head()
print(Sort)

## Series.Tail Method 
## Like how we Have head() which prints top 5 can customize its Just a Similar kind off one 

## DESCRIBE METHOD
##these in row wise gives the mean ,standard deviation max ,min,25% Everything 
print("The Summmary of DataSet Nba.csv by Describe Methos:")
print(data.describe())

## Selecting and Slicing 
# dropping passed columns
## data.drop(["Team", "Weight"], axis = 1, inplace = True)

## Extracting Information From Row  
data1=pd.read_csv("Pandas/nba.csv",index_col="Name")
second = data1.loc["R.J. Hunter"] 
# retrieving rows by loc method 
rows = data.loc["Avery Bradley":"Isaiah Thomas"] 

print("/n /n",rows) 

## How Add a New Row into The CSV File 
new_row = pd.DataFrame({'Name':'Geeks', 'Team':'Boston', 'Number':3,
                        'Position':'PG', 'Age':33, 'Height':'6-2',
                        'Weight':189, 'College':'MIT', 'Salary':99999},
                                                            index =[0])
# simply concatenate both dataframes
data = pd.concat([new_row, data]).reset_index(drop = True)
data.head(5)