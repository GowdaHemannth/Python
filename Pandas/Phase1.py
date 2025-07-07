import pandas as pd
import numpy as np

data=np.array(['a','b','c','d'])
## Panda Series Type
Series=pd.Series(data)
print("Pandas Series",Series)

## Pandas DataFrame
df=pd.DataFrame()
print(df)
lst=['Geeks','for','Geeks','Python','portal','for']
Datafrme=pd.DataFrame(lst)
print(Datafrme)
## Pandas Dataframe from Dictionary 
dict={'name':['aparna','Hemanth','Gowda','Rahul'],
        'Degree': ["MBA", "BCA", "M.Tech", "MBA"],
            'score':[90, 40, 80, 98]}
Name=pd.DataFrame(dict)
print(Name)

## Create Pandas UsinG ZIP
name=['Hemanth','raj','Shamnth']
Age=['21','23','24']
## Once Just Print the list_of_tuples to get the Idea abpu tthese 

list_of_tuples=list(zip(name,Age))

## Now Converting Those Two Lists into One List 
DF=pd.DataFrame(list_of_tuples,columns=['name','Age'])
print(DF)

## Accesssing the Data 
data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
ser = pd.Series(data)
print(ser[:5]) ## Here these Gives Elemnts Till 5 

## When you Want the Particular Elements from list
s=pd.Series(data,index=[10,11,12,13,14,15,16,17,18,19,20,21,22])
print(s[10])

## .loc and .iloc Elements 
H=pd.read_csv("Employee.csv")
s=pd.Series(H['Name'])
## Here .loc Gives Elemnts From 1 to 3
p=s.loc[1:3]   
## Here Where as Iloc it works on Position
g=s.iloc[1:4] ## Here it Excludes 4 

## Binary Operations Posible
ser1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
ser2 = pd.Series([4, 5, 6], index=['A', 'B', 'C'])
Sum=ser1.add(ser2) 
## Like these Other Binary Funcions Are Posiible Here 

## We can Select Multiple Files Also Here 
first=data[["Age","Salary"]]

## Selecting Particular Row with Column 
## Here as you can see we selected row by names of Avery BRadely and selected Column by Team Number and Position 
selection = data.loc[["Avery Bradley", "R.J. Hunter"], ["Team", "Number", "Position"]]
print(selection)

## Slecting All row But Only Specific Columns 
all_rows_specific_columns = data.loc[:, ["Team", "Position", "Salary"]]
print(all_rows_specific_columns)


## Slecting Specific Row import pandas as pd
data = pd.read_csv("/content/nba.csv", index_col="Name")
row = data.iloc[3]
print(row)

## Selcting Particluar Row and column 
selection = data.iloc[[3, 4], [1, 2]]
print(selection)

## Slecting Particular column 
column =data[["Age","Salary"]]

## Writting the Query to get the Answer 
result = data.query("Age > 25 and College == 'Duke'")
print(result)