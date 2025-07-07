import pandas as pd
import numpy as np 
## Here we are Doing Operations with Csv File 
DF=pd.read_csv("Pandas/people_data.csv")
print(DF)

## Printing Name and Eamil
Name=pd.read_csv("Pandas/people_data.csv",usecols=["First Name","Email"])
print(Name)

## How to Write in A Csv with The Raw Data 
# Sample data stored in a multi-line string
data = """totalbill_tip, sex:smoker, day_time, size
16.99, 1.01:Female|No, Sun, Dinner, 2
10.34, 1.66, Male, No|Sun:Dinner, 3
21.01:3.5_Male, No:Sun, Dinner, 3
23.68, 3.31, Male|No, Sun_Dinner, 2
24.59:3.61, Female_No, Sun, Dinner, 4
25.29, 4.71|Male, No:Sun, Dinner, 4"""

# Save the Data to a CSV File
## Here What Happens Here Means It will Create CSV FILE Where data will be Created 
 
with open ("sample.csv",'w') as file:
    file.write(data)
print(data)

## How Much do you Want to get The Information if you you want to Get First Three rows or Column 
dat=pd.read_csv("Pandas/people_data.csv",nrows=3)
## You can also Skip Row to get the Actuall Rows Like Skip Rows 3,4 
## You can Just Paste the Link than Actually Read the Csv File 
url = "https://media.geeksforgeeks.org/wp-content/uploads/20241121154629307916/people_data.csv"
Read=pd.read_csv(url)

## Saving Dict or List ,Dataframes into a CSV File 
name=["Hemanth","Sudarsh","Shashank","Bhuvan"]
deg=["Engineering","Engineering","MBBS","MBBS"]
score=['90','98','99','98']

## Converting it into Dict 

Dict ={"Name":name,"Degree":deg,"Score":score}
DataFrame=pd.DataFrame(Dict)
DataFrame.to_csv('file1.csv')

## you can also save it to the  Specific Location 
# saving the dataframe
## df.to_csv(r'C:\Users\Admin\Desktop\file3.csv')

    