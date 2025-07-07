## Grouping the Data 
import pandas as pd
import numpy as np 

data=pd.read_csv("Pandas/nba.csv")

## Here we are Grouping the Data According to Name
print(data.groupby(['Name','Age']).groups)

## You can Calculate The Sum of Age 
print(data.groupby(['Name','Age']).sum())

## You can Group the Specific Names Here 
Names=data.groupby('Name')
print(Names.get_group('Jeff Green'))

## Grouping 
## Here as you can see You can Gruop by Team And Find out the Mean 

## !! These One is Very Good 

total_Team=data['Age'].groupby(data['Team'])
print(total_Team.mean())

## You Can Also Learn ABout Column Learn that Later 

## !! Mergining ,Joining ,Concatatinating 

## Concatinating 
data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

data2 = {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
         'Age': [17, 14, 12, 52],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

df=pd.DataFrame(data1,index=[0,1,2,3])
df1=pd.DataFrame(data2,index=[4,5,6,7])
frames=[df1,df]
res1=pd.concat(frames)
print(res1)

## Now You Want Only Those Which are Having Common Among them to Using Join
res=pd.concat([df,df1],axis=0,join='inner')
print(res)

### Mergining is Similar to the Joins is Similar to the Sql things 
## It only Gives As Output which as Commnon Things in them 
data1={'Key':['k0','k1','k2','k3'],
       'Name':['Hemanth','Raj','Kausahal','Singham'],
       'Age':[21,23,24,26]}

data2 = {'Key': ['K0', 'K1', 'K2', 'K3'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}
df=pd.DataFrame(data1)
df1=pd.DataFrame(data2)
print("Data1",df,"Data 2",df1)
res=pd.merge(df,df1,on='Key')
print(res)

## Merge Method  Join Name       Description 
## Left          Left outer Join    Use Only keys from the Left Table 
## Right         Right Outer Join   Use Only keys from the Right Table 
##  Outer and inner Study Ones 
## Outer is like it will Give you the Whole DataFrame not like only Common Elemnt will be there 
## But Inner is Like it Will Give the Elemnts which are Having Common Elemnts 

##Pandas Series.str.cat() to concatenate string
## Here we are Using NBA CSV file 
## Question 1 this example, the Team column is concatenated at the end of Name column with separator ", ". The Name column is overwritten with the new series and the data frame is then displayed.
data=pd.read_csv("Pandas/nba.csv")
## Making the Copy of the Team 
new=data['Team'].copy()
## Here we are not Erasing the Column "Name"and overwritting it with Team But We are adding those 
## "Team" and "Name Together " and seperate them using ,
data['Name'] =data['Name'].str.cat(new ,sep=',')
print(data)

## Question Number 2 
## Handling the Null Values while using cat if there is null values it will be compasinated with na_rep
na_string="No College"
data['College']=data['College'].str.cat(new,sep=',',na_rep=na_string)
print(data)

## New topic Append or Add in Dataframes 
##Question 1 Append to Dataframe of Different Shapes

# Creating the first Dataframe using dictionary
df1 = pd.DataFrame({"a":[1, 2, 3, 4],
                    "b":[5, 6, 7, 8]})

# Creating the Second Dataframe using dictionary
df2 = pd.DataFrame({"a":[1, 2, 3],
                    "b":[5, 6, 7],
                    "c":[1, 5, 4]})

df1=df1.append(df2,ignore_index="True")
print(df1)
