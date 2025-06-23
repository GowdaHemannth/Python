## Here we are Gonna Learn Loops
# While loops 
from __future__ import print_function

count=0
while(count<3+1): ## Here These 3+1 States that Means Equal 
    print(count)
    count=count+1
else:
    print("The Code Limit Has been Reached ")


## For loop
n=4
for i in range(0,n,1): ## here it indicates starting from 0 ends to n than incrementimg by 1 
    print(i)

## Loops Through Various Data Structures 
li=([" Name ","Hemanth Gowda","Array"])
for i in range(0,len(li),1):
    print(li[i])

## Nested Loops 
for i in range(1,5,1):
    for j in range (0,i,1):
        print(i,end=" ")

    print()       ## How do we Use Satement after For Statement 

## How to iterare     