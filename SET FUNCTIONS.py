# SETS ARE UNORDERED , UNCHANGEABLE , AND UNINDEXED .

# EXAMPLE OF THE SET .

a = { "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" }
print(a)
print ( type(a) )

# SET DO NOT ACCEPT DUPLICATE VALUES .

b = { "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" , "ONE" , "TWO" }
print(b)

# CHECK THE LENGTH OF THE SET .

a = { "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" }
print ( len(a) )

b = { "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" , "ONE" , "TWO" }
print ( len(b) )

# SET WITH VALUES OF INTEGER DATA TYPE .

c = {11,12,13,14,15,16}
print(c)

# SET WITH VALUES OF FLOAT DATA TYPE .

d = { 1.44 , 1.96 , 2.56 , 3.24 , 4.00 , 4.84 }
print(d)

# SET WITH VALUES OF COMPLEX DATA TYPE .

e = { 11j + 11 , 12j + 12 , 13j + 13 , 14j +14 , 15j +15 , 16j +16 }
print(e)

# SET WITH VALUES OF BOOLEAN DATA TYPE .

f = { True , False , True , False , True , False }
print(f)

# SET WITH VALUES OF STRING DATA TYPE .

a = { "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" }
print(a)

# SET WITH VALUES OF MIXED DATA TYPE .

g = { "SEVEN" , "EIGHT" , 17 , 18 , 5.76 , 6.76 , True , False , 17j + 17 , 18j + 18 }
print(g)
print ( type(g) )

# THE SET CONSTRUCTOR .

c = set ((11,12,13,14,15,16))
print(c)

# THE " set ((11,12,13,14,15,16)) " IS SAME AS THE " {11,12,13,14,15,16} " .

 # LOOP THROUGH SET ITEMS USING for LOOP .

a = { "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" }
for x in a:
    print(x)

# CHECK IF THE ITEM EXIST IN THE SET .

h = { 121 , 144 , 169 , 196 , 225 , 256 , 289 , 324 , 361 , 400 , 441 , 484 }

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

# ADDITION OF THE SET ITEMS .

# add() FUNCTION 

a = { "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" }
a.add("SEVEN")
print(a)

# update() FUNCTION 

a = { "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" }
c = {11,12,13,14,15,16}
a.update(c)
print(a)

# REMOVAL OF THE SET ITEMS .

# remove() FUNCTION

a = { "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" }
a.remove("SIX")
print(a)

# discard() FUNCTION

a = { "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" }
a.discard("SIX")
print(a)

# pop() FUNCTION 

a = { "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" }
a.pop()
print(a)

# clear() FUNCTION 

a = { "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" }
a.clear()
print(a)

# del FUNCTION

a = { "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" }
del a

# JOIN THE LIST USING union() .

a = { "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" }
c = {11,12,13,14,15,16}
k = a.union(c)
print(k)

# JOIN THE LIST USING update() .

a = { "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" }
c = {11,12,13,14,15,16}
a.update(c)
print(a)

# intersection_update() IS USED TO KEEP ONLY THE COMMON ITEMS OF BOTH SETS .

m = {32,34,36,38,40,42,44,46,48,50}
n = {42,44,46,48,50,52,54,56,58,60}
m.intersection_update(n)
print(m)

# intersection() IS USED TO RETURN NEW SET BY KEEPING ONLY THE COMMON ITEMS OF BOTH SETS .

m = {32,34,36,38,40,42,44,46,48,50}
n = {42,44,46,48,50,52,54,56,58,60}
p = m.intersection(n)
print(p)

# symmetric_difference_update() IS USED TO KEEP ALL ITEMS BUT NOT THE COMMON ITEMS OF BOTH SETS .

m = {32,34,36,38,40,42,44,46,48,50}
n = {42,44,46,48,50,52,54,56,58,60}
m.symmetric_difference_update(n)
print(m)

# symmetric_difference() IS USED TO RETURN NEW SET BY KEEPING ALL ITEMS BUT NOT THE COMMON ITEMS OF BOTH SETS .

m = {32,34,36,38,40,42,44,46,48,50}
n = {42,44,46,48,50,52,54,56,58,60}
p = m.symmetric_difference(n)
print(p)

# difference_update() IS USED TO KEEP ONLY ITEMS THAT ARE PRESENT IN SET ONE BUT NOT PRESENT IN SET TWO AS WELL AS NOT THE COMMON ITEMS OF BOTH SETS . 

m = {32,34,36,38,40,42,44,46,48,50}
n = {42,44,46,48,50,52,54,56,58,60}
m.difference_update(n)
print(m)

m = {32,34,36,38,40,42,44,46,48,50}
n = {42,44,46,48,50,52,54,56,58,60}
n.difference_update(m)
print(n)

# difference_update() IS USED TO RETURN NEW SET BY KEEPING ONLY ITEMS THAT ARE PRESENT IN SET ONE BUT NOT PRESENT IN SET TWO AS WELL AS NOT THE COMMON ITEMS OF BOTH SETS . 

m = {32,34,36,38,40,42,44,46,48,50}
n = {42,44,46,48,50,52,54,56,58,60}
p = m.difference(n)
print(p)

m = {32,34,36,38,40,42,44,46,48,50}
n = {42,44,46,48,50,52,54,56,58,60}
p = n.difference(m)
print(p)

# COPY THE SET USING FUNCTION copy() .

a = { "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" }
q = a.copy()
print(q)

# COPY THE SET USING BUILD IN METHOD set() .

a = { "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" }
r = set(a)
print(r)