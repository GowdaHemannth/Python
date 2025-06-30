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