import numpy as np 
import matplotlib.pyplot as plt

# Your plotting code here
# Data: [Restaurant_Id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],
    [2, 120000, 160000, 200000, 230000],
    [3, 180000, 200000, 240000, 270000],
    [4, 100000, 130000, 160000, 190000],
    [5, 170000, 190000, 210000, 250000]
])

print( "=== Zomatao Sales Analyese===")

## Sample Data for first three Elemnt 
print(" The First Three Elements",sales_data[0:3])

## THe sales But Dont Want the IDS 
print("Sales Data but Dont Want the IDs ",sales_data[:,:1])

## Total Sales Per Year 
print(np.sum(sales_data,axis=0)) ## THese Gives The first Column Sum

## The Main Thing is Axis 0 means We are Calculating the Sum Along column means y axis which is 0 
## If we Want to Calculate the Sum along the X axis we need to aDD It Along X Axis 
Yearly_Total=np.sum(sales_data[:,1:],axis=0)
print(Yearly_Total)

## Calculate the min Sales

Min=np.min(sales_data[:,1:],axis=1)
print(Min)

## Maximum Sales Per Year 
Max=np.max(sales_data[:,1:],axis=0)
print(Max)

## Average Sales Per Year 
Avg=np.mean(sales_data[:,1:],axis=0)
print(Avg)

## np.cumsum() stands for cumulative sum.
 ## It returns a new array where each element is the sum of all previous elements up to that point.
 
CumSum=np.cumsum(sales_data[:,1:],axis=1)
print(CumSum)

## Plotting Just For Example 
plt.figure(figsize=(10,6))
plt.plot(np.mean(CumSum,axis=0))
plt.title("Average Cumulative Sales Across Restaurent") 
plt.xlabel("years")
plt.ylabel("sales")
plt.grid(True)
plt.show()     

## Vector Analysis
vEctor1=np.array([1,2,3,4,5])      
vEctor2=np.array([6,7,8,9,10])    

print(" The Vector Addition",vEctor1+vEctor2)
print("The Vector Multiplication",vEctor1*vEctor2)  

## Dot product
print("The Dot product",np.dot(vEctor1,vEctor2))  

## Angle Recovery
angle = np.arccos(
    np.dot(vEctor1, vEctor2) / (np.linalg.norm(vEctor1) * np.linalg.norm(vEctor2))
)
print(angle)

## Vectorised Activity 
restaurent_Types=np.array(["Biriyani","Chiniese","Pizza","Burger","Cafe"])
vectorised_upper=np.vectorize(str.upper)
print("Vectorized Upper",vectorised_upper(restaurent_Types))

## BroadCasting 
## Here it Takes Each value in the row or Column Divided Each value by 12 
monthly_Avrage=sales_data[:,1:]/12
print(monthly_Avrage)
                  