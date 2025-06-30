## Here We are Going to use Some advance Level of The Python Concept 
## Searching in the Python is much easier 
print(3 in [1,2,3]) ## Here it Returns True if the Value Really Present in the Array List 

if 's' in 'geeksforgeeks':
    print("Yes The KeyWord S is Present ")
else:
    print('Print That Keyword is Doesnt not Present in the Keyword ')

## Checking if the Two Elemnts or Identical or Not 
a=[1,2,3]
b=a 
print(a is b) ## Here it returns True  

## The Python begins 
for num in range(0,10 +1,1): ## To Include the Things i can Actually Use thse 10+1 Symbol like these 
    if num==0:
     print("The Number 2 is Found ")
    else:
       print(num)

 # Usage of the While Loop 
i=0
while i<=5:
    i+=1
    if(i==3):
       break
    else:
       print(i)
      
n = 10
for i in range(n):

    # pass can be used as placeholder
    # when code is to added later
    pass
        
a,b=4,0
try:
   print(a//b)  ## if You are Getting Error and you dont know exactly Where youbare Getting Error 
# Then Add the Try and Execpt Method Here
except Exception:
   print(" You Cant Divide these ")   
           
# Assert You are Here Having A b Value as Zero But But you are sayign b should not be Equal to zero if zero stop the code#
# assert b!=0, " B is Zero"           

## I ftwo Strings Are Not Identical 

# temp="geeksforgeeks"
# if(temp!="geeks"):
  # raise("Both the Strings Are Not Eqaul ")

## From Now Defining The Function How do it Works 
def func():
   yield 3  # Its Like A Brother TO the Return Statement Here it Gives The Output One by One 
   yield 4

func()  # Here You Just Need to call The Function not Like in Java Where you Simply Add Everything 
for value in func():  # Than you need to Pass These Statement 
    print(value)

# Async aWait Function Implementation 

# Think that you Have Writtten a Function to Download the Mp4  File or SomethignLike these 
# You need wait till the Funtion Executes to continue tothe Function 

## Sqare Root Finding In the Python 
g=lambda x:x*x*x
print(g(7))

## List is also Like Array But Here you can also add String Type and Integer
a=[1,2,3,'Hemanth ',"Gowda "]

## Set DaAT Structure Same as the Set Data Structure in the JAVA 
s1=set("GeeksforGeeks")
print(s1) ## Here now output Will be of Nonn Duplicate NStrings Values 

s2=set(["Geeks","for","Geeks"])
print(s2)## Hereyou will get only two elements Those are Geeks and for 

## How to Iterate It Over the Loop
for i in s2:
   print(i,end='') ## Here end is Used to just add space 

 ## Dictionary Similar Function as Map 
d={}  
d={1:"Geeks","Name":"For",3:"Geeks"}
print(d["Name"]) ## How get the VAlues 
print(d[3]) ## Another Way Getting the VAlue Here 

## ternary operation 
Marks=45

res="Pass" if Marks>=45 else "fAil"
print(res)
