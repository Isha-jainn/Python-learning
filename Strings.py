#About Strings

a="Behave like a boss"
print("a=Behave like a boss")
print("The type of a is " ,type(a))    
print("The length of a is " ,len(a))     

#Indexing and slicing 

print(a[:])
print(a[1:])
print(a[:5])
print(a[0])
print(a[4])
print(a[-3:-1])
print(a[-1])  
print(a[:-1])

#Operators
print('o' in a)
print('t' not in a)

print("\nTo show the concatenation using '+' operator")
b="Computer"
c="Science"
print("b = 'Computer")
print("c = 'Science")
d = b+c 
print("The concatenation is ",d)

print("\nTo show repetion using '*' operator")
st="fun"
st1 = st*3  
print(st1)

print("\nTo show the use of '%' format specifier")
print('%s'%(st)) 
print('%s   %s'%(st,d))
print('Have',st)


#String Functions.
string='Whats Up'
string1='heya'
string2='9743'
string4=' '

print(string.lower())  
print(string.upper())
print(string1.capitalize()) 
print(string.count('U'))  
print(string.isupper()) 
print(string.islower())  
print(string.index('s')) 
print(string.isalnum()) 
print(string.isnumeric()) 
print(string2.isdecimal())
print(string2.isdigit()) 
print(string4.isspace()) 
