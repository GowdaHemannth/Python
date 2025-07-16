## Advantages right we all know Gives Accurate Predictiona and Learn from the Pattern and Domains
## Disadvantages Overfitting and feature Extraction requires lot of time 
## So Hyperparameter Tuning Means Adjusting the  Parameters of the Model which are Not Tarined During the Training Phase 
## What is Best Fit Line for the Model Wheee the error is Minimum Like in the predcted Value and the Observed Value 
##  The Difference Between the Predicted and actual value is Called  Cost Lost Function 
## Gradient Descent is the Algorithm which is Used to Minimize the Cost Function and Help to Find the Best Fit Line 
## Eavluation metrices is Used to Evaluate the model Performances 
## 1 Mean Sqaue Error 2 mean Absolute Error 
## Regularising the Model Process of Reducing the Overfitting of the Model it Can be Done by Adding Penalty Terms 

## Here The My Intenstion of These is To Find the Other one like first we will feed correspndimf data 

## For example think we are feeding the data of child ageas x and thier immunity on y then it will give 
## After feeding certain Daat set now for Prediction Now i will feed child age then __-->>"THESE ALGO WILL PREDICT THE Y "
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.axes as ax
from matplotlib.animation import FuncAnimation
Data=pd.read_csv("C:/Users/Heman/OneDrive/Desktop/data_for_lr.csv")
New_Data=Data.dropna() ## Here Dropping the Null Values 
Train_Input=np.array(New_Data.x[0:500].reshape(500,1))
Train_Output=np.array(New_Data.y[0:500].reshape(500,1))
Test_Input=np.array(New_Data.x[500:700].reshape(199,1))
Test_Output=np.array(New_Data.y[500:700].reshape(199,1))

## Now In Linear Regression Here y=mx+c 
class LinearRegression:
    def __init__(self):
        self.parameters={} ## Here we are Storing The M and c Value 
        
    def forwardPrediction(self,Train_input):
        m=self.parameters['m']
        c=self.parameters['c']
        ## Here we are Predicting the Value for the y=mx+c 
        prediction=np.multiply(m,Train_input)+c
        return prediction    
    ## Here we are Calculating the Cost Function Mean Error for the 
    ## prediction value- Original Value 
    def Cost_Function(self,Tarin_Output,prediction):
        cost=np.mean((Train_Output-prediction)**2)
        return cost
    
    ## Here in Backward Propagation We are Calculaing the Error then we are Calculating the 
    ## Respective slope in order to minimise the Error then intercept in Order to Calculate the C 
    def Backward_Propagation(self,Train_Input,Train_Output,predictions):
        derivatives={} ## Here we are Creative list 
        df=predictions-Train_Output
        dm=np.mean(np.multiply(df,Train_Input))
        dc=np.mean(np.multiply(df))
        derivatives['dm']=dm
        derivatives['dc']=dc
        return derivatives
    
    ## Here after calculating the Backward Propgation Now Its time to updaate the dm and dc 
    
    def updateParameters(self,derivatives,lerning_rate=0.01):
        self.parameters['m']=self.parameters['m']-lerning_rate*derivatives['m']
        self.parameters['c']=self.parameters['c']-lerning_rate*derivatives['c']
        
    def train(self, train_input, train_output, learning_rate, iters): 
        self.parameters['m'] = np.random.uniform(0, 1) * -1
        self.parameters['c'] = np.random.uniform(0, 1) * -1

        self.loss = [] 

        fig, ax = plt.subplots() 
        ## Here we are setting the X value what should be Minimum waht should be Maximum 
        x_vals = np.linspace(min(train_input), max(train_input), 100) 
        ## Here we are PLotting the Predicted Regression Line with Red line with x =x+value then y=self.parameters['m'] * x_vals + self.parameters['c'],
        line, = ax.plot(x_vals, self.parameters['m'] * x_vals + self.parameters['c'], color='red', label='Regression Line') 
        ## Here we are plotting the Original Data set values 
        ax.scatter(train_input, train_output, marker='o', color='green', label='Training Data') 

        ax.set_ylim(0, max(train_output) + 1) 
        
        
        def update(frame): 
            predictions = self.forward_propagation(train_input) 
            cost = self.cost_function(predictions, train_output) 
            derivatives = self.backward_propagation(train_input, train_output, predictions) 
            self.update_parameters(derivatives, learning_rate) 
            line.set_ydata(self.parameters['m'] * x_vals + self.parameters['c']) 
            self.loss.append(cost) 
            print("Iteration = {}, Loss = {}".format(frame + 1, cost)) 
            return line, 



        ani = FuncAnimation(fig, update, frames=iters, interval=200, blit=True) 
        ani.save('linear_regression_A.gif', writer='ffmpeg') 
        
        plt.xlabel('Input') 
        plt.ylabel('Output') 
        plt.title('Linear Regression') 
        plt.legend() 
        plt.show() 

        return self.parameters, self.loss 
    