import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import plotly.express as px
Data1 = pd.read_csv("C:/Users/Heman/OneDrive/Desktop/df1.csv")
Data2=pd.read_csv("C:/Users/Heman/OneDrive/Desktop/df2.csv")
## These Gives the Line Plot Graph 
## Data1.plot()
## plt.show()

## Second One Gives the Area Graph 
##Data2.plot.area(alpha=0.4)
##plt.show()

## Third one Gives Bar Graph 
## Data1.plot.bar()
##plt.show()


## SIMILARY YOU CAN GET THE HISTOGRAM AND THE SCATER MANY MORE AND YOU CAN CUSTOMIZE YOUR GRAPH LIKE 
## AXIS AND STYLE OF LINE AND THE BOUNDARY EVERYTHING YOU CAN ACTUALLY DO THAT 

## Now we are looking plotly vizualisation 
df=px.data.iris()
## These just take sepal length in y axis for the Evaluation thing and genearte the Graph 
## These for the Line Garph Thing 
 ##fig = px.line(df,  y='sepal_length',line_dash='species',color='species') ## Here we use the line group as one of parameter then it will differentiate between the differnt types of Species aAvailble 
## Here Species will get differntiated with Species Name and with color also 


## Now if we want it for the bar Graph 
data=px.data.tips()

## fig = px.bar(data, x='day', y="total_bill", color='sex',
   ##          facet_row='time', facet_col='sex')
## Here in these Bar Graph it Shows in row time like Dinner or lunch or BreakFast 
## column male or Female 
## fig.show()


## Now we are Gonna Talk About Pie Chart 
## Here values total Bill Means THe Amount That spent on the Each day the total amount
 ## fig=px.pie(data,values='total_bill',names='day')
 
 ## Based on the Darker the Colour the More the Money Spent on that Day 
fig = px.pie(data, values="total_bill", names="day",
             color_discrete_sequence=px.colors.sequential.RdBu,
             opacity=0.7, hole=0.5)
fig.show()