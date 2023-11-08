# TUPLES ARE ORDERED , CHANGEABLE , AND INDEXED .

# EXAMPLE OF THE LIST .

a = [ "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" ]
print(a)
print ( type(a) )

# LIST ALSO ACCEPT DUPLICATE VALUES .

b = [ "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" , "ONE" , "TWO" ]
print(b)

# CHECK THE LENGTH OF THE LIST .

a = [ "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" ]
print ( len(a) )

b = [ "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" , "ONE" , "TWO" ]
print ( len(b) )

# LIST WITH VALUES OF INTEGER DATA TYPE .

c = [11,12,13,14,15,16]
print(c)

# LIST WITH VALUES OF FLOAT DATA TYPE .

d = [ 1.44 , 1.96 , 2.56 , 3.24 , 4.00 , 4.84 ]
print(d)

# LIST WITH VALUES OF COMPLEX DATA TYPE .

e = [ 11j + 11 , 12j + 12 , 13j + 13 , 14j +14 , 15j +15 , 16j +16 ]
print(e)

# LIST WITH VALUES OF BOOLEAN DATA TYPE .

f = [ True , False , True , False , True , False ]
print(f)

# LIST WITH VALUES OF STRING DATA TYPE .

a = [ "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" ]
print(a)

# LIST WITH VALUES OF MIXED DATA TYPE .

g = [ "SEVEN" , "EIGHT" , 17 , 18 , 5.76 , 6.76 , True , False , 17j + 17 , 18j + 18 ]
print(g)
print ( type(g) )

# THE LIST CONSTRUCTOR .

c = list ((11,12,13,14,15,16))
print(c)

# THE " list ((11,12,13,14,15,16)) " IS SAME AS THE " [11,12,13,14,15,16] " .

'''
THE 4 TYPES OF ARRAYS IN PYTHON ARE:
1. LIST
2. TUPLE
3. SET
4. DICTIONARY
'''

# SLICING AND INDEXING IN LIST .

h = [ 121 , 144 , 169 , 196 , 225 , 256 , 289 , 324 , 361 , 400 , 441 , 484 ]

print ( h[4] )
print  ( h[-4] )

print ( h[5:9] )
print ( h[-9:-5] )

print ( h[:7] )
print ( h[:-4] )

print ( h[6:] )
print ( h[-5:] )

print( h[::2] )
print ( h[::3] )

print( h[3:11:2] )
print ( h[-8:-2:2] )

# CHECK IF THE ITEM EXIST IN THE LIST .

h = [ 121 , 144 , 169 , 196 , 225 , 256 , 289 , 324 , 361 , 400 , 441 , 484 ]

if 256 in h:
    print("YES")
else:
    print("NO")    

if 240 in h:
    print("YES")
else:
    print("NO")

print ( 256 in h )

print ( 240 in h )      

# CHANGE THE SINGLE ITEM VALUES OF THE LIST .

k = [ "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" ]  
print(k) 

k[6] = "ITALY"
print(k)

# CHANGE THE MULTIPLE ITEM VALUES OF THE LIST .

k = [ "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" ] 
print(k)

k[2:5] = [ "HUNGARY" , "LATVIA" , "ROMANIA" ]
print(k)

# CHANGE OF SINGLE VALUE BY REPLACING IT WITH MULTIPLE VALUES .

k = [ "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" ] 
print(k)

k[5:6] = [ "ESTONIA" , "LATVIA" , "MALTA" ]
print(k)

# CHANGE OF MULTIPLE VALUES BY REPLACING IT WITH SINGLE VALUE .

k = [ "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" ] 
print(k)

k[2:5] = [ "ROMANIA" ]
print(k)