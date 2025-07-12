import numpy as np
import pandas as pd
import sklearn
from sklearn import datasets
## These Helps in Spliting the Data which is Used to Make Predictions 
from sklearn.model_selection import train_test_split
## For standardszsaton and Normalization we are Using the Data Preprocessing 
from sklearn.preprocessing import StandardScaler
##
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

## Here Testing Data Sets 
iris=datasets.load_iris()
X=iris.data
y=iris.target

## Splitting the Data Sets 
X_Train,X_Test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
## Here 0.3 Means Traning 30 % Data 70 % Data For Testing 

## Standardizing Features 
scaler=StandardScaler()
X_Train=scaler.fit_transform(X_Train)
X_Test=scaler.transform(X_Test)

## Now Feeding it to the Model 
log_reg=LogisticRegression()
log_reg.fit(X_Train,y_train)

## Making the Prediction for the Testing Data Set 
y_pred=log_reg.predict(X_Test)

## Now 
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


## Oaky Here Now i have trained a model Now 

## Prediction time 
new_flowers = [
    [5.0, 3.4, 1.5, 0.2],
    [6.2, 2.9, 4.3, 1.3],
    [6.5, 3.0, 5.5, 1.8],
    [4.9, 3.1, 1.5, 0.1],
    [5.8, 2.7, 4.1, 1.0]
]
## Now standarsing the Data 
new_flowers_scalesd=scaler.transform(new_flowers)
new_preds=log_reg.predict(new_flowers_scalesd)
for i, pred in enumerate(new_preds):
    print(f"Flower {i+1}: Predicted species → {iris.target_names[pred]}")
    
    
    ## " COLUMN TRANFORMER " 
    # Categorial Data  Here like NAmes string numerical will be age Income Etc 
from sklearn.compose import ColumnTransformer
## Here   SimpleImputer fill the Missing value with Mean value 
## originalencoder 0 and 1
## oneHotEncoder() Convert Categories into 0s and 1s
## # we have declared transformer and called ColumnTransformer() method
#we use SimpleImputer for speed and t1 as parameter,t2 for OrdinalEncoder i.e for categorical values and t3 for one hot encoding i.e for Gender and City.
##transformer = ColumnTransformer(transformers=[
  ##  ('t1',SimpleImputer(),['Speed']),
   ## ('t2',OrdinalEncoder(categories=[['low','high']]),['Average_speed']),
    ##('t3',OneHotEncoder(sparse=False,drop='first'),['Gender','City'])
##],remainder='passthrough')
## These remainder passthrough leave the Remaining has it is 
df = pd.read_csv('Geeksforgeeks/Data/diabetes.csv')
print(df.head())