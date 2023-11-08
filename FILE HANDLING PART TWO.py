'''

# OPEN THE FILE OBJECT .

a = open ( "FILETWO.txt" , "r" )
print ( a.read() )
a.close()

# OPEN THE FILE AND APPEND THE CONTENT OF THE FILE .

b = open ( "FILETWO.txt" , "a" )
b.write ( "\nMY FULL NAME IS KULDEEP YADAV" )
b.close()

# CHECK THE FILE .

c = open ( "FILETWO.txt" , "r" )
print ( c.read() )

# OPEN THE FILE AND OVER WRITE THE CONTENT OF THE FILE .

d = open ( "FILETWO.txt" , "w" )
d.write ( "ROHIT SHARMA \nVIRAT KOHLI \nSHUBMAN GILL \nKULDEEP YADAV \nRAVINDRA JADEJA" )
d.close()

# CHECK THE FILE .

e = open ( "FILETWO.txt" , "r" )
print ( e.read() )
e.close()

# "x" MODE IS USED TO CREATE A NEW FILE .

# CREATE A NEW FILE .

f = open ( "FILETHREE.txt" , "x" )
f.close()

# WRITE THE CONTENT IN THE FILE .

g = open ( "FILETHREE.txt" , "w" )
g.write ( "JOE BIDEN \nTOM CRUISE \nALAN WAALKER \nJUSTIN BIEBER" )
g.close()

# CHECK THE FILE .

h = open ( "FILETHREE.txt" , "r" )
print ( h.read() )
h.close()

# DELETE THE FILE .

import os
os.remove ( "FILETHREE.txt" )

# CHECK IF THE FILE EXISTS OR NOT EXISTS .

import os
if os.path.exists ( "FILETHREE.txt" ) :
    os.remove ( "FILETHREE.txt" ) 
else:
    print ( "THE FILE DOES NOT EXISTS" )    

# DELETE THE EXISTING FOLDER .

# rmdir FUNCTION ALSO KNOWN AS REMOVE DIRECTORY REMOVES ONLY EMPTY FOLDER .

import os
os.rmdir("NEWFOLDER")

'''