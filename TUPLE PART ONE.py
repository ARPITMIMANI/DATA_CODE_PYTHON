# TUPLES ARE ORDERED , UNCHANGEABLE , AND INDEXED .

# EXAMPLE OF THE TUPLE .

a = ( "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" )
print(a)
print ( type(a) )

# CHECK THE LENGTH OF THE TUPLE .

a = ( "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" )
print ( len(a) )

b = ( "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" , "ONE" , "TWO" )
print ( len(b) )

# TUPLE WITH VALUES OF INTEGER DATA TYPE .

c = (11,12,13,14,15,16)
print(c)

# TUPLE WITH VALUES OF FLOAT DATA TYPE .

d = ( 1.44 , 1.96 , 2.56 , 3.24 , 4.00 , 4.84 )
print(d)

# TUPLE WITH VALUES OF COMPLEX DATA TYPE .

e = ( 11j + 11 , 12j + 12 , 13j + 13 , 14j +14 , 15j +15 , 16j +16 )
print(e)

# TUPLE WITH VALUES OF BOOLEAN DATA TYPE .

f = (True , False , True , False , True , False )
print(f)

# TUPLE WITH VALUES OF STRING DATA TYPE .

a = ( "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" )
print(a)

# TUPLE WITH VALUES OF MIXED DATA TYPE .

g = ( "SEVEN" , "EIGHT" , 17 , 18 , 5.76 , 6.76 , True , False , 17j + 17 , 18j + 18 )
print(g)
print ( type(g) )

# THE TUPLE CONSTRUCTOR .

c = tuple ((11,12,13,14,15,16))
print(c)

# THE " tuple ((11,12,13,14,15,16)) " IS SAME AS THE " (11,12,13,14,15,16) " .

# CREATE A TUPLE WITH ONE ITEM ONLY .

h = ("JUSTINBIEBER",)
print(h)
print ( type(h) )

# EXAMPLE OF NOT A TUPLE .

k = ("ALANWALKER")
print(k)
print ( type(k) )

# SLICING AND INDEXING IN TUPLE .

m = ( 121 , 144 , 169 , 196 , 225 , 256 , 289 , 324 , 361 , 400 , 441 , 484 )

print ( m[4] )
print  ( m[-4] )

print ( m[5:9] )
print ( m[-9:-5] )

print ( m[:7] )
print ( m[:-4] )

print ( m[6:] )
print ( m[-5:] )

print( m[::2] )
print ( m[::3] )

print( m[3:11:2] )
print ( m[-8:-2:2] )

# CHECK IF THE ITEM EXIST IN THE TUPLE .

m = ( 121 , 144 , 169 , 196 , 225 , 256 , 289 , 324 , 361 , 400 , 441 , 484 )

if 256 in m:
    print("YES")
else:
    print("NO")    

if 240 in m:
    print("YES")
else:
    print("NO")

print ( 256 in m )

print ( 240 in m )   

# CHANGE THE ITEM VALUES OF THE TUPLE .    

n = (  "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" ) 
print(n)

# STEP 1 : CHANGE FROM TUPLE TO LIST .
   
print ( type(n) )
p = list(n)
print ( type(p) )

# STEP 2 : CHANGE THE VALUES OF THE LIST .

p[7] = "ROMANIA"
print(p) 

# STEP 3 : CHANGE FROM LIST TO TUPLE .

q = tuple(p)
print ( type(q) )
print(q)

# ADDING THE ITEM VALUES IN THE TUPLE .

n = (  "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" ) 
print(n)

# STEP 1 : CHANGE FROM TUPLE TO LIST .

print ( type(n) ) 
p = list(n)
print ( type(p) )

# STEP 2 : ADDING THE VALUES TO THE LIST .

p.append("ITALY")
print(p) 

# STEP 3 : CHANGE FROM LIST TO TUPLE .

q = tuple(p)
print ( type(q) )
print(q)

# ADDING TWO TUPLES USING "+" .

c = (11,12,13,14,15,16)
d = ( 1.44 , 1.96 , 2.56 , 3.24 , 4.00 , 4.84 )
c = c + d
print(c)

# REMOVING THE ITEM VALUES IN THE TUPLE .

n = (  "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" ) 
print(n)

# STEP 1 : CHANGE FROM TUPLE TO LIST .

print ( type(n) ) 
p = list(n)
print ( type(p) )

# STEP 2 : REMOVING THE VALUES TO THE LIST .

p.remove("FINLAND")
print(p) 

# STEP 3 : CHANGE FROM LIST TO TUPLE .

q = tuple(p)
print ( type(q) )
print(q)

# DELETE A TUPLE USING del FUNCTION .

n = (  "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" ) 
del n

# PACKING A TUPLE MEANS ASSIGNING VALUES TO THE TUPLE .

r = ( "BLUE" , "YELLOW" , "GREEN" , "ORANGE" , "BROWN" , "RED" )
print(r)

# UNPACKING A TUPLE MEANS EXTRACTING VALUES FROM THE TUPLE .

# CASE ONE

r = ( "BLUE" , "YELLOW" , "GREEN" , "ORANGE" , "BROWN" , "RED" )
( r1 , r2 , r3 , r4 , r5 , r6 ) = r

print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(r6)

# CASE TWO 

s = ( "PURPLE" , "YELLOW" , "GREEN" , "ORANGE" , "BROWN" , "RED" , "SILVER" , "VIOLET" , "GREY" , "BLUE" )
( s1 , s2 , s3 , *s4 , s5 , s6 ) = s

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)

# TUPLE ALSO ACCEPT DUPLICATE VALUES .

t = ( "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" , "ONE" , "TWO" )
print(t)