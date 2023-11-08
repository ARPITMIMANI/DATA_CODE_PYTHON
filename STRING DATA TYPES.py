# SINLGE LINE STRINGS . 

a = "MY NAME IS JUSTIN BIEBER"
print(a)

b = 'MY NAME IS ALAN WALKER'
print(b)

# MULTIPLE LINE STRINGS .

c = ''' 
LIST OF COUNTRIES IN EUROPE ARE:
01. GERMANY 
02. DENMARK 
03. ITALY
04. NORWAY
05. SWEDEN
06. FINLAND
07. BELGIUM
08. CROATIA
09. LATVIA
10. AUSTRIA
11. POLAND
12. ROMANIA 
'''
print(c)

# STRING ARE ARRAYS .

d = "WHEN YOU GIVE JOY TO OTHER PEOPLE , YOU GET MORE JOY IN RETURN ."

print (d[6])
print (d[-4])

# LENGTH OF STRINGS .

a = "MY NAME IS JUSTIN BIEBER"
print ( len(a) )

b = 'MY NAME IS ALAN WALKER'
print ( len(b) )

c = ''' 
LIST OF COUNTRIES IN EUROPE ARE:
01. GERMANY
02. DENMARK 
03. ITALY
04. NORWAY
05. SWEDEN
06. FINLAND
07. BELGIUM
08. CROATIA
09. LATVIA
10. AUSTRIA
11. POLAND
12. ROMANIA
'''
print ( len(c) )

d = "WHEN YOU GIVE JOY TO OTHER PEOPLE , YOU GET MORE JOY IN RETURN ."
print ( len(d) )

# CHECK STRING USING in .

d = "WHEN YOU GIVE JOY TO OTHER PEOPLE , YOU GET MORE JOY IN RETURN ."

print ( "JOY" in d )
print ( "joy" in d )
print ( " JOY" in d )
print ( "Joy" in d )
print ( "JOY " in d )
print ( "JO" in d )
print ( "," in d )
print ( ";" in d )
print ( "GIVE JOY" in d )
print ( "GIVE  JOY" in d )

# CHECK STRING USING if AND in .

d = "WHEN YOU GIVE JOY TO OTHER PEOPLE , YOU GET MORE JOY IN RETURN ."

if "JOY" in d:
    print("YES")
else:
    print("NO")    

if "joy" in d:
    print("YES")
else:
    print("NO")    

# CHECK STRING USING not in .

d = "WHEN YOU GIVE JOY TO OTHER PEOPLE , YOU GET MORE JOY IN RETURN ."

print ( "JOY" not in d )
print ( "joy" not in d )
print ( " JOY" not in d )
print ( "Joy" not in d )
print ( "JOY " not in d )
print ( "JO" not in d )
print ( "," not in d )
print ( ";" not in d )
print ( "GIVE JOY" not in d )
print ( "GIVE  JOY" not in d )     

# CHECK STRING USING if AND not in .

d = "WHEN YOU GIVE JOY TO OTHER PEOPLE , YOU GET MORE JOY IN RETURN ."

if "JOY" not in d:
    print("YES")
else:
    print("NO")    

if "joy" not in d:
    print("YES")
else:
    print("NO")

# SLICING AND INDEXING IN STRING .

d = "WHEN YOU GIVE JOY TO OTHER PEOPLE , YOU GET MORE JOY IN RETURN ."

print (d[11:21])
print (d[-10:-6])

print (d[11:31:2])
print (d[-24:-3:3])

print (d[:17])
print (d[15:])

print (d[:-12])
print (d[-14:])