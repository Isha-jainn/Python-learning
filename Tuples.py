#Tuples in python

#creating a tuple
tuple1=("yes","no","true")
print(tuple1)

#Accessing tuple items
print(tuple1[1])

#Access items using loop
for x in tuple1:
    print(x)
    
    
if "false" in tuple1:   #to check if a particular item is present in tuple
    print("\nyes")
    
print(len(tuple1))     #to calculate length of a tuple

#Tuple functions

del tuple1         #to delete the tuple completely

#Tuple Constructor--to create a tuple
tuple2=tuple(("1","you"))
print(tuple2)