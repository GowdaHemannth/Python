import pandas as pd
import numpy as np
import xlsxwriter as xl
import os

df = pd.DataFrame({'Data': ['Geeks', 'For', 'geeks', 'is',
                               'portal', 'for', 'geeks']})
writter=pd.ExcelWriter('pandasEx.xlsx',engine='xlsxwriter')

## Write Data Frame to the ExelSheet
df.to_excel(writter,sheet_name='sheet1')
writter.save()
print(writter)

## We can transform multiple DataFarmes into Single Excel Sheet Thing 
df1=pd.DataFrame({'Data':[11,12,13,14,15]})
df2=pd.DataFrame({'Data':[16,17,18,19,20]})
df3=pd.DataFrame({'Data':[21,22,23,24,25]})
writter=pd.ExcelWriter('pandasEx.xlsx',engine='xlsxwriter')

df1.to_excel(writter,sheet_name='sheet1')
df2.to_excel(writter,sheet_name='sheet2')
df3.to_excel(writter,sheet_name='sheet3')
writter.close()
os.startfile('pandasEx.xlsx')


## Excel Numericals SET 2 
from datetime import datetime,date

DataFrame=pd.DataFrame({
    'Date and Time':[datetime(2018,1,11,11,30,55),
                     datetime(2018,2,12,1,20,33),
                     datetime(2018,3,13,11,10,9),
                      datetime(2018, 4, 14, 16, 45, 35),
                      datetime(2018, 5, 15, 12, 10, 15)],
       'Dates only':    [ date(2018, 6, 21),
                      date(2018, 7, 22),
                      date(2018, 8, 23),
                      date(2018, 9, 24),
                      date(2018, 10, 25) ],
    
})

## Now after Getting the Data
## Create a Excel Sheet Thing 
writer_object=pd.ExcelWriter("Example_datetime.xlsx",
                             engine='xlsxwriter',
                              datetime_format ='mmm d yyyy hh:mm:ss',
                        date_format ='mmmm dd yyyy')

## After Creating WorkSheet Naming the Excel Sheet 
DataFrame.to_excel(writer_object,sheet_name='Sheet1')


worksheet_object=writer_object.sheets['Sheet1']

worksheet_object.set_column('B:C',20)
writer_object.save()