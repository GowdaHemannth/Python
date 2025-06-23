## Here we are gonna Pass Function as a Argument 

def fun(func,arg):
     return func(arg) #
def square(x): #
    return x**2

ans=fun(square,5)
print(ans)

## Constructor usage in the Python 
class Person:
    def __init__(self, name, age):  # ✅ constructor
        self.name = name
        self.age = age

    def greet(self):  # ✅ method
        print(f"My name is {self.name} and age is {self.age}")  # ✅ f-string

# Object creation and method call
p1 = Person("hemanth", 30)
p1.greet()

## Returning function usage in the python 
def is_true(a):
    return bool(a)

ans=is_true(2<5)
print(ans)

## We can return multiple values in the Pytgon 
def func():
    name="Hemanth "
    age=30
    return name,age

n,a=func()
print("My name is ", n, " and age is ",a)

## Updating in the String is also Posiible in the Present Python 
s="GFG"
s1=s+s[0] ## Updating 
print(s1)

## String Slicing extrcting the Strings 
s2="GEEKSFORGEEKS"
print(s2[1:2]) ## Here you will get the values from the Indeses staring from 0 index to the 1 index 
print(s2[:2]) ## From zero to 1 
print(s2[3:]) ## From three 
## Delteing is del " String name "

name="Hemanth "
age=25
print(f"My name is:{name} and age is :{age}") ## That f Alphabet is Very Important 

## Checking if particular word is Present in the String or Not 
s="GeeksForGeeks"
print("geeks" in s)

def Func(*args):
    return sum(args)

print(Func(1,2,3,4))