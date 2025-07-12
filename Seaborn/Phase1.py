import seaborn as sns
import matplotlib.pyplot as plt
## seaborn is the Extension of Matplotlib Garph Thing
## Graph 1  
##sns.set_theme()
tips=sns.load_dataset("tips")
##sns.relplot(data=tips,x="total_bill",y="tip",col="time",hue="smoker",style="smoker",size='size')
## Here hue Means based on Category if its the Smoker it will give red Color ,and blue color 
##plt.show()

##dots=sns.load_dataset("dots")
##sns.relplot(
 ##   data=dots, kind="line",              # line plot (not scatter)
  ##  x="time", y="firing_rate",           # x: time, y: neuron activity
   ## col="align",                         # separate plots for stimulus vs response
    ##hue="choice",                        # color by T1/T2 choice
   ## size="coherence",                    # line thickness changes by coherence
   ## style="choice",                      # line style (solid/dashed) by choice
 ##   facet_kws=dict(sharex=False),        # allow different x-axis range for each subplot
##)
## These for DistributionalData the Displot 
# Here in these Data we use col for different ones like dinner and Lunch 
##sns.displot(data=tips,x='total_bill',col='time')
## ----> The Most intersting Part Here is if you mention kind=kde plot,hist gram plot it show onlt that Parts To you 
## ----->>> But if you Show write kind='kde as true then it will "Show Both Histogram and KDE Plot Together "
##plt.show()

## Now for categorila data catplot()
##sns.catplot(data=tips,x='day',y='total_bill',kind='violin',hue='smoker',split=True)## Here hue Differentiate Between the 
## Smoker and the Non Smoker 
##plt.show()

## --->> Joint Plot Here As you Can see Distribution betwenthe Two Numericals 
## it can be Scatter plot any and on top kde plot for x axis on Left Kde plot for Y axis 
penguins=sns.load_dataset('penguins')
##sns.jointplot(data=penguins,x="flipper_length_mm", y="bill_length_mm", hue="species")
##plt.show()


## "PairPlot()" Here what Happens Means think you have four Variables it will gwt the Garph for those variavles like 
## firt body weight versus hieght then body mass veruses hieght 
##sns.pairplot(data=penguins,hue='species')
##plt.show()
## You can use Differnt Plots Like histplot()---> kdeplot()
## In Single X axis IF you Plot these like Col=species then you need to more X axis 
##sns.displot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
##plt.show()

## Drawing graph or the Long form of the Data 
##Flights_Details=sns.load_dataset("flights")
##sns.kdeplot(data=Flights_Details,x="year",y="passengers",hue="month",kind="kde")
##plt.show()



## Here These Means of year is Not Calculated but the Grouping will be Done by Year Wise and only numeric values 
## Means calculted so along with year only the numeric cotaining column is Number of Passenger so 
## -->> MEAN OF PASSECGERS WILL BE CALCULATED 
##flights_avg = flights.groupby("year").mean(numeric_only=True)



## NEW API CALLED SEABORN OBJECTS APIS 
import seaborn.objects as so

## Its more Fast and Flexible As Compared to the Previous One 
## Here Its Nessecery 
##(
    ## so.Plot(penguins, x="bill_length_mm", y="bill_depth_mm")
    ##.add(so.Dot())
    ##.show() 
##)

## You can Add the Color and the Size of the Points Here like 
## .add(so.Dot(color='g,size=4))

## Mapping Properties 
##(
 ## so.Plot(penguins,x='bill_length_mm',y='bill_depth_mm',pointsize='body_mass_g').add(so.Bar()).show()
  ## Here Point Size will be Defined Based on the body_mass 
  
##)


##
(
  so.Plot(penguins,x="species",y="body_mass_g",color="sex").add(so.Bar(),so.Agg()).show() ## Here Aggreagate Means think 
    ## it Has two species named same name so there aggregate means /2
    ## If want male and Female in Differnt Things then its SimPLe By so.Dodge() 
)
## ---->>> Important if you Add "ORIENT =Y" Graphs Bars on HORIZONATL 