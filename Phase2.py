##  Numpy Array Operations
import numpy as np;

arr=np.array([1,2,3,4,5])
print("Basic Slicing ",arr[2:4]) 
print("     Stepswise Like leaving One Element or Two Element",arr[1:5:2])

## Slicing and Indexing in 2D Array 
arr_2d=np.array([[1,2,3],[4,5,6]])
## Specific Element
print("Specific Element First mention Row ",arr_2d[1,2])
# arr_2d[1,2] These Menas 1st Row Second Element
print("Entire Row",arr_2d[1])
print("Entire Column",arr_2d[:,1])
## Sorting 
unsorted_array=np.array([3,4,6,2,1,8,9])
print("Get the Sorted Array",np.sort(unsorted_array))
arr_2D_Unsorted=np.array([[3,2],[1,2],[2,3]])
## column sortAxis =0     The Row ##Axis =1 Sort
print("Sorted 2D Array",np.sort(arr_2D_Unsorted,axis=0              ))
##Filtering 
numbers=np.array([1,2,34,5,6,7,8,9,10])
even_Number=numbers[numbers%2==0]
print(even_Number)

## Filter With Mask 
mask=numbers>5
print("Numbers Greater than 5   ",numbers[mask])

## Fancy Indexing vs np.where()
indices=[0,2,4]
print(numbers[indices])

where_result=np.where(numbers>5)
print("NP Where",numbers[where_result])

## Np.where Also Creates The Array But with The Specific Condition 
Condition_Array=np.where(numbers>5,numbers*2,numbers)
print(Condition_Array) ## Here you Have the Array Where Numbers are Greater than 5 and Numbers with Multiply with 2

##Adding And Removing Data 
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
combined=arr1+arr2 ## Array gets Added
combined_1=np.concatenate((arr1,arr2)) ## These Adds The Array likE(1,2,3,4,5,6)
print(combined_1 )

## Arry Compatability
a=np.array([1,2,3])
b=np.array([4,5,6,7])
c=np.array([7,8,9])
print("Compatability Shapes",a.shape==b.shape)

## Some Operations
Original=np.array([[1,2],[3,4]])
new_one=np.array([5,6])

## Here VStack Helps Us to Add tHe new Row
with_new_row=np.vstack((Original,new_one))
print(Original) 
print(with_new_row)    

## Helps t Add the Column 
new_col=np.array([[7,],[8]])
col=np.array([9])
 ## Ones Run These Go know the Value 
with_new_Col=np.hstack((new_col,Original))
print(" The New Column Adde ",with_new_Col)

## Deletes
arr=np.array([1,2,3])
deleted=np.delete(arr,2)
print("The Array After Delete",deleted)