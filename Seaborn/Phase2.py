import seaborn as sns
import matplotlib.pyplot as plt
import seaborn.objects as so

## Here these is the Continuation Part of the Graph 
## Building And Displaying the Graph 
tips=sns.load_dataset("tips")
##(
  ##  so.Plot(tips, x="total_bill", y="tip")
  ##  .add(so.Dots())
   ## .add(so.Line(), so.PolyFit()) ## Here It will Generate the Dots And Line in the Single Graph 
   ## .show() ## Compute the Regression Line Reduces the Noisy Values and Remove Dirty values 
##)

## Topic 2 Facilating And Pairing the Subplots 
## in the Normal Graph Techniques and in the seaborn techniqies we used col='' something to Differentiate the 
## Column  Based on the Values but here you need to add .faciet()
penguins=sns.load_dataset('penguins')
##(
  #  so.Plot(penguins,x="flipper_length_mm").facet("species").add(so.Bars(),so.Hist()).show()
##)

## And one more Thing here is .facet(col='species',row='sex') ## Here You can Add Both species thing and row sex value thing 

## 3rd Topic is Integrateing with Matplotlib 
import matplotlib.pyplot as plt
import matplotlib as mpl
##Here think you Want Histogram in the Left and Scatter Plot on the Right 
## Seaborn Actsully Dont Support THese So Matplotlib is Been used 
f = mpl.figure.Figure(figsize=(8, 4))  ## Here it does Create the Empty Block 
sf1,sf2=f.subfigures(1,2) ## Here Figure Divides the Figure into 2 Parts 
(
    so.Plot(penguins,x="body_mass_g",y="flipper_length_mm")
    .add(so.Dot()).on(sf1).plot()
)
(
    so.Plot(penguins, x="body_mass_g")
    .facet(row="sex")
    .add(so.Bars(), so.Hist())
    .on(sf2)
    .plot() 
)
plt.show()


### 4th Topic Visualizing the Statistical Data 
### Here we are Seeing new Parameter Named error Bar if it is None than Dont Show any error bar 
fmri = sns.load_dataset("fmri")
## here in replot it have two options scatter,relplot and catplot have two options kde and bar 
sns.relplot(
    data=fmri, kind="line",
    x="timepoint", y="signal", errorbar="sd", ## Now here that Error is sd Means it will Stands sd 
    
)
plt.show()

### sns.displot(tips, x="day", shrink=.8)
##These thing is Used to get the Width Between the Two Distributional Bars 

##Now we are Looking for the 2D Histogram
sns.displot(x="") ## Here if i mention y axis also then it will be of 2 Dimenstionl Histogram 
## Same thing Will Follow Up for the Kde Plot Also 



## Expalination About the Graphs Here Lets Say Like Histogram Here is 2d Histogram Sice it is A 2d Thing here we will 
## ##will Get the 2D Histogram in the Center and top boxplot for x axis 
## RIght boxplot for the Y axis 
g = sns.JointGrid(data=penguins, x="bill_length_mm", y="bill_depth_mm")
g.plot_joint(sns.histplot)
g.plot_marginals(sns.boxplot)