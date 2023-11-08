# ADDITION OF THE LIST ITEMS .

# append() FUNCTION 

a = [ "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" ] 
a.append("MEXICO")
print(a)

# insert() FUNCTION 

a = [ "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" ] 
a.insert ( 4 , "CANADA" )
print(a)

# extend() FUNCTION 

a = [ "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" ] 
b = [ "MEXICO" , "CANADA" , "ITALY" , "JAPAN" ]
a.extend(b)
print(a)

# REMOVAL OF THE LIST ITEMS .

# remove() FUNCTION 

a = [ "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" ] 
a.remove("POLAND")
print(a)

# pop() FUNCTION 

a = [ "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" ] 
a.pop(3)
print(a)

a = [ "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" ] 
a.pop()
print(a)

# del FUNCTION 

a = [ "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" ] 
del a[1]
print(a)

a = [ "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" ] 
del a

# clear() FUNCTION 

b = [ "MEXICO" , "CANADA" , "ITALY" , "JAPAN" ]
b.clear()
print(b)