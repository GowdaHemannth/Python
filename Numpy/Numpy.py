## Numpy array and Basics 
import numpy as np 
import time   
arr_ld=np.array([1,2,3,4,5])
print(arr_ld) 
   
 ## Numpy versusu the List   
start=time.time()
py_list=[1,2,3]
print("Pytho list Multiplication ",py_list*2,"Time is ",time.time()-start)  
np_array=np.array([1,2,3])
start=time.time()
print("Numpay Multiplication",np_array*[2],"Time is ",time.time()-start)  ## Th ematrix Gets Mutiplied  

## Creating Array From Strch 
zeros=np.zeros((3,4))   ## Here You will get the mtrix of 3 row and  column Matrix
print(zeros)   
## Ones Array np.ones()          

full=np.full((2,2),7) ## Constant Arrya of 7

random=np.random.random((2,3))
print(random)

## Sequence Array with Starting Point From 0 to till 10 with Incremnet Values of 2

sequence=np.arange(0,10,2)

## Vector matrices Tensor
vector=np.array([1,2,3])
matrix=np.array([[1,2,3],[2,3,4]])
print(matrix)       

## Array properties 
arr=np.array([1,2,3])
print('Shape ',arr.shape)
print('Dimensions ',arr.ndim)
print('Size ',arr.size)
print('Data Type ',arr.dtype)

## Array Reshaping 
arr= np.arange(12) ## Array from 1 to 12 
reshaped=arr.reshape((3,4)) ## Now that Array Will get Shaped to 3d Array
print(" THe reshped array is ",reshaped)
## You have Faltten from 2d Arry to 1 dimentsional Array

## Ravel return the original arry Modification 
## But in the Palce of Faltten it return Copy of Array
raveld=reshaped.ravel()
print("The ravel ",raveld)

## Can get the Transpose of the Matrix 
## A =      [[1, 2, 3],
       ##   [4, 5, 6]]
## Transpose of the Above MATRix is  
## Aᵀ =     [[1, 4],
  ##        [2, 5],
   ##       [3, 6]]
   
Transpose =reshaped.T
print(" ThE tarnspose matrix is ",Transpose)
      

