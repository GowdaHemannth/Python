## Pandas.apply Function used to give the Sum value 
import pandas as pd
import numpy as np
df = pd.DataFrame({
    'math': [80, 90],
    'science': [85, 95]
})
## Here what Happens is will get Total of Math and Science 
## Total will be in New Column 
## Here you need write the Function And Mention the Axis
def Calculation(row):
    return row['math'] + row['science']

df['Total']=df.apply(Calculation,axis=1)
print(df)
df['Total']=df.apply(np.sum,axis=1)
print(df)

## Time series 
series=pd.Series([11,21,2,1,3,8,4,21,23,24])
##Here Periods number of numbers in operations and freq do you want it to change according to the Yearly or Monthly or Day
index_=pd.date_range('2010-10-09 08:45', periods=10,freq='Y')
## Here series data was Assigned to the Index one 
series.index=index_
print(series)

## Here you can also ind out Max,Min,Sum
df=pd.read_csv("Pandas/nba.csv")
print(df.aggregate({"Number":['sum', 'min'], 
              "Age":['max', 'min'], 
              "Weight":['min', 'sum'],  
              "Salary":['sum']}))

## You can Also get the Mean Value 

print(df.mean(axis=0))

## While Creating Series Indexing also Nesseceray 
DataSeries=pd.Series([10,1,2,3,4,5])
index_ = ['Coca Cola', 'Sprite', 'Coke', 'Fanta', 'Dew', 'ThumbsUp']
DataSeries.index=index_
print(DataSeries)
print(DataSeries.mean())

## It Also Gives Mean Absolute Deviation which Means The Distance Between Two Points And Mean of it

## !!! Important These Was Removed From Pandas 2.0 Versions 
print(df.mad(axis=0))

## Sample Error Mean Gives you the how much Sample Mean expected as Compared to population Mean 
## Its Like STANDARD MEAN / N
print( "  The Sem of Data is  ",df.sem(axis=0))

## Counting the Unique Values  
## In The Values At the Last Column You will get the Column Where you will get the counts 
print(df.value_counts())


## Manipulating The Given Data 
import pandas as pd

# Define a dictionary containing Students data
data = {'Name': ['Pandas', 'Geeks', 'for', 'Geeks'],
        'Height': [1, 2, 3, 4],
        'Qualification': ['A', 'B', 'C', 'D']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# using assign() and passing address list as parameter
df = df.assign(address = ['NewYork', 'Chicago', 'Boston', 'Miami'])

print(df)


## Somewaht Different 
address = {'Pandas': 'NewYork', 'Geeks': 'Chicago', 
            'for': 'Boston', 'Geeks_2': 'Miami'}
## Here now we are Adding one Additional Column to the First Data Set
## Here Name will get Attached according to the Name 
df['address']=df['Name'].map(address)

## You can Add Data at Particular Position 
## 2 Suggest the Column Number and Age Suggests the Column Name And those are the Colun Values 
df.insert(2,"Age",[21,22,23,24])
print(df)

## You an Add New Data 
## Here Based on the Hieght THe Category wll be Asssigned to itself
df.loc[df['Height']>=3,'Category']='Tall'
df.loc[df['Height']<3,'Category']='Short'
print(df)

## Dropping The Row and Column Based on the Name of Column and Row Name 
## IF Axis is 0 Then column if axis is 1 Then Row 
# dropping passed columns
 ## data.drop(["Team", "Weight"], axis = 1, inplace = True)
  
# display
# dropping passed columns
 ## data.drop(["Team", "Weight"], axis = 1, inplace = True) 
 
 
## Iterate Over The Row 
# dictionary of lists
dict = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score': [90, 40, 80, 98]}

# creating a dataframe from a dictionary
 ## df = pd.DataFrame(dict)
df=pd.read_csv("Pandas/nba.csv")
## for i ,j in df.iterrows():
   ## print(i,j)
   ## print() 
   
                 ## Here Column Has Name Axis You knpw that 
             ## !! Here WE Have Special Property inplace if it true Means Original dta gets modifiedof Data Comes else         
df.sort_values("Name", axis=0, ascending=True, inplace=True, na_position='last')   
                                          ## And Here na_Position Means Where the Data IS Not Availble 
  
data.sort_values(["Team", "Age", "Height"], axis=0,
                 ascending=[False,True,False],
inplace=True)             ## Here as you can see Team Column has been given False which means Descending And Age column has been given true Which means Ascending 


## You can aslo Add the Rows inBetween                                  