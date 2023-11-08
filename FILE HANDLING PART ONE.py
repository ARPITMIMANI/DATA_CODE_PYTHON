# open FUNCTION IS USED TO OPEN THE FILE TO GET THE FILE OBJECT .

# FIRST METHOD 

a = open ( "FILEONE.txt" )
a.close()

# SECOND METHOD

b = open ( "FILEONE.txt" , "rt" )
b.close()

# "rt" STANDS FOR READ TEXT .

# "rb" STANDS FOR READ BINARY .
'''

LIST OF MODES FOR OPENING FILE .

"r" -- OPEN AN EXISTING FILE FOR READING .

"w" -- OPEN AN EXISTING FILE FOR WRITING . IT WILL OVER WRITE ANY EXISTING DATA .

"a" -- OPEN AN EXISTING FILE FOR APPENDING . IT WILL NOT OVER RIDE ANY EXISTING DATA .

"r+" -- TO READ AND WRITE DATA INTO A FILE. PREVIOUS DATA IN THE FILE WILL NOT BE ERASED. 
 
"w+" -- TO WRITE AND READ DATA. IT WILL OVER RIDE ANY PREVIOUSLY STORED DATA. 

"a+" -- TO APPEND AND READ DATA FROM A FILE. IT WILL NOT OVER RIDE ANY EXISTING DATA. 

'''

# read FUNCTION READS THE SPECIFIC NUMBER OF CHARACTERS STARTING FROM CURRENT POSITION .

# OPEN THE FILE USING open FUNCTION AND read FUNCTION .

print ( "---- ---- ---- ---- ---- ----" )
c = open ( "FILEONE.txt" , "r" )
print ( c.read() )
c.close()
print ( "---- ---- ---- ---- ---- ----" )

# READ ONLY PARTS OF A FILE .

c = open ( "FILEONE.txt" , "r" )
print ( c.read(100) )
c.close()
print ( "---- ---- ---- ---- ---- ----" )

# readline FUNCTION READS THE CHARACTERS STARTING FROM CURRENT READING POSITION UPTO A NEW LINE CHARACTER .

# readlines FUNCTION READS ALL LINES UNTIL THE END OF THE FILE AND RETURNS A LIST OBJECT .

# READ LINE BY LINE OF THE FILE .

# FIRST METHOD

d = open ( "FILEONE.txt" , "r" )
print ( d.readline() )
print ( d.readline() )
print ( d.readline() )
print ( d.readline() )
print ( d.readline() )
print ( d.readline() )
print ( d.readline() )
print ( d.readline() )
print ( d.readline() )
print ( d.readline() )
d.close()
print ( "---- ---- ---- ---- ---- ----" )

# SECOND METHOD

d = open ( "FILEONE.txt" , "r" )
print ( d.readlines() )
d.close()
print ( "---- ---- ---- ---- ---- ----" )

# LOOPING THROUGH THE FILE LINE BY LINE .

e = open ( "FILEONE.txt" , "r" )
for line in e:
    print(line)
e.close()    
print ( "---- ---- ---- ---- ---- ----" )

# close FUNCTION IS USED TO CLOSE THE FILE OBJECT .

# CLOSE THE CURRENT OPEN FILE .

f = open ( "FILEONE.txt" , "r" )
print ( f.readlines() )
f.close()
print ( "---- ---- ---- ---- ---- ----" )