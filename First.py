from typing import List     
print("Hello ")

if 10>5: ## These Means you know right Simple For loop 
    print("God is Great")
    print('Kohli is Legend ')

    ## How to Take Input from user 
    name=input("Wht is your Name ")
    print("Hello",name,)

    s="Hemanth"
    age=21

    print(s,age)

    ## Conditional If Satetment 
    if age>22:
        print('Engineering Completed .')
    elif age >18 :
        print('License Avaible ')

     ## How can i Convert The Integer Type of these Things
     # is the allignment Needs to be Correct Here if Those and all Falls Here 
    n=int()
    H=2
    Hesaru='Hemanth'
    total=25

    # Same Variable can be Assigned to Two Different Things 
    x=2
    x="Kavya"

    # Same variable can be Used for Initialization of Different Things 
    a=b=c=100

    a,b,c=100

    a,b,c=1 ,"Hemanth",2.5

    # Defig the Functin 
    def func():
        print("T-20")

    func # Access the Function 

    x=10
    del x 

    # Count The Length of the String 
    word="Length"
    L=len(word)
    print(L)

    # SWapping the Values Without Using the Varible value without using third Variable 
    x,y=y,x

    # Here We are Discussing about Various Operations 
    x=10
    y=10
    print(x>y) # These is Enough no need of IF Statement 

    # Define List here
    l: List[int]=[]

x = 24
y = 20
list = [10, 20, 30, 40, 50]

if(x not in list):
    print("Yes X is not present here ")
else:
    print("Yes X is present in the List")   

h= 10
k=90
c=h
print(k is not h) # Here you will get the output has true Because K is not h 

# Ternory Operator 
a,b=10,20
min=a if a<b else b  # Here its stateing if a is less than b than only print the a else print b

## Searching for a Elemnt in A Python is Much More Easier Has Compared to the Jav 
print(3,[1,2,3])