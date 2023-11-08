# CONSIDER A MODULE TO BE AS SAME AS A CODE LIBRARY LIKE A FILE CONTAINING A SET OF FUNCTIONS WHICH IS INCLUDED IN A APPLICATION .

import moduleone

moduleone.fullname ( "TOM" , "CRUISE" ) 
moduleone.fullname ( "JUSTIN" , "BIEBER" )
moduleone.fullname ( "ALAN" , "WALKER" )

# A MODULE CAN CONTAIN VARIABLES OF ALL TYPES .

import moduletwo

a = moduletwo.marksclass10["DAN"]
print(a)

b = moduletwo.marksclass10["LEO"]
print(b)

c = moduletwo.marksclass09["DAN"]
print(c)

d = moduletwo.marksclass09["LEO"]
print(d)

# RENAMING A MODULE USING as KEYWORD .

# EXAMPLE ONE 

import moduleone as one
one.fullname ( "JOE" , "BIDEN" )

# EXAMPLE TWO 

import moduletwo as two

e = two.marksclass10["TOM"]
print(e)

f = two.marksclass09["TOM"]
print(f)

# BUILT IN MODULES .

import platform

g = platform.machine()
print ( "MY MACHINE NAME IS" , g )

h = platform.processor()
print ( "MY PC PROCESSOR NAME IS" , h )

k = platform.python_compiler()
print ( "MY PYTHON COMPILER NAME IS", k )

m = platform.system()
print ( "MY PC OPERATING SYSTEM NAME IS", m )

n =platform.python_version()
print ( "MY PYTHON VERSION IS" , n )

p = platform.platform()
print ( "MY PC PLATFORM NAME IS" , p )

q  = platform.architecture()
print ( "MY PC ARCHITECTURE IS" , q )

# THE dir FUNCTION MECHANISM BEHAVES DIFFERENTLY WITH DIFFERENT TYPES OF OBJECTS AS IT ATTEMPTS TO PRODUCE THE MOST RELEVANT INFORMATION RATHER THAN COMPLETE INFORMATION .

import platform
print ( dir(platform) )

import sys
print ( dir(sys) )

import os
print ( dir(os) )

# from KEYWORD IS USED TO IMPORT ONLY PARTS OF A MODULE .

# EXAMPLE ONE 

from moduletwo import marksclass10
r = marksclass10["TOM"]
print(r)

# EXAMPLE TWO

from moduletwo import marksclass09
s = marksclass09["TOM"]
print(s)

# EXAMPLE THREE

from moduleone import fullname
fullname ( "ROHIT" , "SHARMA" )