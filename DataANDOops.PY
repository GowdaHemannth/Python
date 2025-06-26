## String 
## iteration in String
import itertools 
s="Geeksforgeeks"
for char in s:
    print(char)
## Function s.split() Uses to Split the Word 

## List Data Structure 

a=[1,2,"Hemanth "]
print(type(a[2]))     ## To find out what kind of data
# ;List can be created  by simply like a=[2]*7 now the List will Conatin[2,2,2,2,2]
S=["Hemanth","Gowda","Kuvempuu"] ## Iteration Type1
for s in S:
    print(s)
## Iteration Type2
for i in  range(0,len(S),1):
    print(s[i])
    
## How to iterate Over Multiple List 
num = [1, 2, 3]
col = ['red', 'white', 'black']
val = [255, 256]

for a, b, c in itertools.zip_longest(num, col, val):
    print(a, b, c)
    
        
 ## Third Data Structure is Dictinories 
d={1:'Geeks',2:'Hemanth Gowda',3:" Chikke Gowda "}     
print(d) ## As Simple as Printing 

## Updating and adding in the Dictinories 
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d[1] = "Python dict"

print(d)

## Iteration of 
for key in d:
    print(key)
for value in d.values() :
    print(value )    
## Creatin of set s
set1 = set(["Geeks", "For", "Geeks"])
print(set1)

## Array Data Structure 
a=arr.array('i',[1,2,3])
print(a[0])    
    
## Oops Concepts 
## Creating a Class 
class Dog:
    ## Species is Class Variable 
    species="Pomerian" ## Class attribute same as name and age but this not grouped or clubed together Method 
    def  __init__(self,name,age):
        self.name=name ## Instance Variable 
        self.age=age
## Creating Objects of the Dog
dog1=Dog("Buddy",27) ## The whole Line is a Object But the Buddy is the Instance 
dog2=Dog("Tommy",32)

print(dog1.name)    ## Accesing the Name you can access the Species Name dog1.species 

## Modifying the Instance Variable 
dog1.name="Max"
Dog.species="Flenime" ## Updating the Species name 
## Now the dog1 and dog2 will be Having Same Speciess 

## Inheritance 
# Single Inheritance 
class Dog:
    def __init__(self,name):
        self.name=name
    def display_Nme(self):
        print(f" Dogs Name is :{self.name}")    
        
class Laborator(Dog): ## Inheritance From Dog 
    def sound(self):
        print("Dog Barkas ")        

## Access those Objects 
lab=Laborator("Tommy")
lab.display_Nme()  
lab.sound()

## Multivel inheritance 
class GuideDog(Laborator): ## As you can see GuideDog Inheritance From the Laborator then from calss Dog 
    def Guide(self):
        print("The dog guidess ")
G=GuideDog("Max")
G.display_Nme()
G.Guide()
G.sound()

## Multiple Inheritance 
class Freind(Dog,GuideDog): ## Its multiple inheritance nOT Multilevel Inheritance 
    def Paly(Self):
        print("The dog plays ")           
            