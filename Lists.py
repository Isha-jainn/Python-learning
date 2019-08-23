#ALL ABOUT LISTS IN PYTHON

#Create a list
mylist=["isha","parul","antra"]
print(mylist)

#Access items in list
print(mylist[2])

#Access items using loop
for x in mylist:
    print(x)
    
#change item value
mylist[2]="kanika"
print(mylist)

if "isha" in mylist:   #to check if a particular item is present in list
    print("\nyes")
    
print(len(mylist))     #to calculate length of a list

#List functions
mylist.append("antra")  #to add item at the end of a list
print(mylsit)

mylist.insert(1,"akansha")  #to add item at a particular index
print(mylist)

mylist.remove("akansha")   #to remove a particular item from list
print(mylist)

mylist.pop()    ##to remove last item from the list
print(mylist)

del mylist[2]   #to delete particular item from list
print(mylist)

list1=mylist.copy()   #to copy list in another list
print(list1)

del list1         #to delete whole list

mylist.clear()    #it empties the list
print(mylist)