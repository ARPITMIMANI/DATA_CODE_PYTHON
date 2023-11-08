# CHECK THE DATA TYPES OF THE VARIABLES .

a1 = 16
b1 = 19.36
c1 = 3j + 4
d1 = 10 + 0j

print ( type(a1) )
print ( type(b1) )
print ( type(c1) )
print ( type(d1) )

# int DATA TYPE .

a2 = 4294967296
b2 = -68719476736             
c2 = 0

print ( type(a2) )
print ( type(b2) )
print ( type(c2) )

# float DATA TYPE .

# float IS ALSO KNOWN AS FLOATING POINT NUMBER .

a3 = 27.04
b3 = -23.04
c3 = 81.0000
d3 = 49.
e3 = 0.0
f3 = -0.

print ( type(a3) )
print ( type(b3) )
print ( type(c3) )
print ( type(d3) )
print ( type(e3) )
print ( type(f3) )

# float NUMBERS CAN ALSO BE SPECIFIC NUMBERS LIKE "e" OR "E" WHICH MEANS POWER OF 10 .

a4 = 32.64e14
b4 = 48.36E8
c4 = -40.96e12
d4 = -70.56E10
e4 = 64e24
f4 = 56e36

print ( type(a4) )
print ( type(b4) )
print ( type(c4) )
print ( type(d4) )
print ( type(e4) )
print ( type(f4) )

# complex DATA TYPE

# complex NUMBERS ARE WRITTEN WITH "j" AS THE IMAGINARY PART .

a5 = 10j + 6
b5 = 14 + 8j
c5 = 18.64j
d5 = -16.72j
e5 = 12 + 0j
f5 = -4 + 0.0j

print ( type(a5) )
print ( type(b5) )
print ( type(c5) )
print ( type(d5) )
print ( type(e5) )
print ( type(f5) )

# TYPE CONVERSION 

a6 = 144
b6 = 77.44
c6 = 36j + 16

print(a6)
print ( type(a6) )

print(b6)
print ( type(b6) )

print(c6)
print ( type(c6) )

# CONVERT FROM int DATA TYPE TO float DATA TYPE .

d6 = float(a6)
print(d6)
print ( type(d6) )

# CONVERT FROM float DATA TYPE TO int DATA TYPE .

e6 = int(b6)
print(e6)
print ( type(e6) )

# CONVERT FROM int DATA TYPE TO complex DATA TYPE .

f6 = complex(a6)
print(f6)
print ( type(f6) )

# CONVERT FROM float DATA TYPE TO complex DATA TYPE .

g6 = complex(c6)
print(g6)
print ( type(g6) )

# RANDOM NUMBER 

# PRINT ANY RANDOM INTEGER NUMBER BETWEEN 1 TO 10 ONLY .

import random
print ( random.randrange (1,11) )