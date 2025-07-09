import seaborn as sns
import matplotlib.pyplot as plt
import seaborn.objects as so
##tips = sns.load_dataset("tips")
##sns.catplot(data=tips, x="day", y="total_bill",kind='swarm',hue='sex')

##plt.show()

## You can also Write Query 
  ## sns.catplot(data=tips.query("size != 3"), x="size", y="total_bill", native_scale=True)
  ## Here you need to get the Data Which are Not Equal to 3
tips = sns.load_dataset("tips")
##sns.regplot(x="total_bill", y="tip", data=tips)
## plt.show()

## Here we are Taking abaout the Anscoems Quartlet 
## These Mean it will have same Mean "SAME VARIANCE ","SAME CORRELATION","SAME LINEAR REGRESSION "
##anscombe = sns.load_dataset("anscombe")

##sns.lmplot(x="x", y="y", col="dataset", col_wrap=2,
 ##          data=anscombe, ci=None, scatter_kws={"s": 50})
##plt.show()

## You Can also get the Garphs Using JoinPlot 

## Here you can get the jointplot like Histogram and Reg and regression Line that shows Positive Correlation 
## Negative Correlation
##sns.jointplot(data=tips,x='total_bill',y='tip',kind='reg')
##plt.show()

## You Can also get the PairPlot 
##sns.pairplot(tips,x_vars=["total_bill","size"],y_vars=["tip"],kind='reg')
##plt.show()

## ------->>>>>> Here you will get the Upper Class Elemnts where you can Choose which one Should be Upper Class and Whic
##-------->>> Which one Should be lower And Which One Should Be Diagonal 
iris = sns.load_dataset("iris")
g=sns.PairGrid(iris)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
g.map_diag(sns.kdeplot)
plt.show()  