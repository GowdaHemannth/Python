import pandas as pd
import numpy as np
from datetime import date
## Working on 1) DateTime 2) Text Data 3) Csv file to Excel
d=date(2025,7,4)
print(d)

## Time Stamp 
timestamp = pd.Timestamp('2023-10-04 15:30:00')
year=timestamp.year
print(year)
## Like these You can Type Month, Date ,Time ,Hour,WeekDay

## You Can get the Time According to the Differnt Time Stamps Accros World With of America And Other Regions 

## Working with Text Data 
## Str.UpperCase and Str.LowerCase
##  Now we are Going to Work on str.split Function 
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Knnuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 

df=pd.DataFrame(data)

## How to Drop null Values 
df.dropna(inplace="True")

##              Here We are Going to Split the Adreess At the Position at letter a    
df["Address"]=df['Address'].str.split("a",n=1,expand=True)

## Question 2
                  ## Here we are Gonna Repalce Age with 25 and Repalce it With the String Twenty Five
data["Age"]= data["Age"].replace(25.0, "Twenty five")
# creating a filter for age column 
# where age = "Twenty five"
filter = data["Age"]=="Twenty five"
 
# printing only filtered columns
data.where(filter).dropna()



## Working With the Csv File 

