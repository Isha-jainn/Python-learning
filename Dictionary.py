#Dictionary in Python

#Creating a dictionary
mydict = {
        "Company" : "Oriflame",
        "Product" : "Cosmetics",
        "Year" : 1995}
print(mydict)

#Accessing itmes of a dictionary
s = mydict["Company"]  #key name should be mentioned
print(s)

#Another method for accessing items in a dictionary
p = mydict.get("Company")
print(p)

mydict["Product"] = "Wellness"   #to change an item
print(mydict)

for m in mydict:     #to print all key names
    print(m)
    
for m in mydict:
    print(mydict[m])
    
for m , n in mydict.items():  #to print keys and values together
    print(m , n)

if "Year" in mydict:     #to check the existence of an item
    print("\nyes")
    
print(len(mydict))     #to calculate length of a dictionary

#to add items
mydict["Designation"] = "Diamond Director"
print(mydict)

#Dictionary Functions
mydict.pop("Designation")   #to remove a particular item
print(mydict)

mydict.popitem()     #to remove last inserted item
print(mydict)

dict1 = mydict.copy()     #to copy a dictionary 
print(dict1)

del mydict["Company"]   #to delete a particular item
print(mydict)

mydict.clear()    #it empties a dictionary
print(mydict)

del mydict   #to delete the whole dictionary
