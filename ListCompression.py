nums=[1,2,3,4,5,6,7,8,9]

## Copy these to other List 
##my_list=[]
##for n in nums:
  ##  my_list.append(n)
## print( my_list)

## Another Way of Copying the Elemnts 
my_list=[n for n in nums] 
print(my_list)
## Here i want a Letter Alphabet Pair Like a0 b1 c2 

mylist=[]
for n in "abcd":
    for num in nums: 
        mylist.append((n,num))
print(mylist)        
##Another Way is mylist=[(letter,num) ffor letter in "abcd" for num in nums]

## Dictinary Compressions 
names=['Bruce','Clark','Peter','Logan','Wade']
heros=['Batman','Superman','Spiderman','Wolverine','Deadpol']
zipped= zip(names,heros)
print(list(zipped))
## Zip unction is Used to Map the Elemnst 

## How to write tose in a Simple Way 
my_dict={}
for name,hero in zip(names,heros):
    my_dict[name]=hero
print(my_dict)   
## To get the Key and Values like Hashmp
for key,value in my_dict.items():
    print(key,value) 
    
    
    
 ## Set Compresions 
Num=[1,2,2,3,3,4,5,6,6,8,8,9,10]
my_set=set()
for n in nums:
    my_set.add(n)
print(my_set)    
   