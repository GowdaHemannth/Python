import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
Data=pd.read_csv("C:/Users/Heman/OneDrive/Desktop/WineQT.csv")

## Here We are Discusiing about the Steps in EDA Process 
## Analyse the Shape 
##Data.shape()
##Data.info() ## Describe theInformation 
##Data.describe() ## Here you will Get the Mean Value ,Median Value 
##Data.columns.tolist() ## Here you will Convert the Data to to list 
##Data.isnull().sum()
##Data.nunique() ## Here you will get the Uniques Values 
quality_counts = Data['quality'].value_counts()

plt.figure(figsize=(8, 6))
plt.bar(quality_counts.index, quality_counts, color='deeppink')
plt.title('Count Plot of Quality')
plt.xlabel('Quality')
plt.ylabel('Count')
plt.show()


## Feature Engineering it is techinques of Converting the Raw Data into the Useful Data 
## Here it inclueds Selecting The impoetant Feature 