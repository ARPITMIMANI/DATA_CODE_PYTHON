# LOOP THROUGH THE LIST .

a = [ "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" , "SEVEN" , "EIGHT" , "NINE" , "TEN" ]
for x in a:
    print(x)

# LOOP THROUGH THE STRING .

b = "WATERMELON"
for x in b:
    print(x)

# THE break STATEMENT .

# FIRST CASE 

print ("THE BREAK STATEMENT FIRST CASE")
a = [ "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" , "SEVEN" , "EIGHT" , "NINE" , "TEN" ]
for x in a:
    if x == "SIX" :
        break
    print(x)

# SECOND CASE    

print ("THE BREAK STATEMENT SECOND CASE")
a = [ "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" , "SEVEN" , "EIGHT" , "NINE" , "TEN" ]
for x in a:
    print(x)
    if x == "SIX" :
        break

# THE continue STATEMENT .

print ("THE CONTINUE STATEMENT")
a = [ "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" , "SEVEN" , "EIGHT" , "NINE" , "TEN" ]
for x in a:
    if x == "SIX" :
        continue
    print(x) 
        
# THE range FUNCTION .  

# PRINT ALL INTEGERS FROM 0 TO 10 .

print ("ALL INTEGERS FROM 0 TO 10")
c = range(11)
for x in c:
    print(x) 

# PRINT ALL INTEGERS FROM 11 TO 20 .

print ("ALL INTEGERS FROM 11 TO 20")
d = range(11,21)
for x in d:
    print(x)       

# PRINT ALL MULTIPLES OF 4 FROM 11 TO 50 .

print ("ALL INTEGERS WHICH ARE MULTIPLES OF 4 FROM 11 TO 50")
e = range(12,50,4)
for x in e:
    print(x) 

# THE else STATEMENT .

print ("ALL INTEGERS WHICH ARE MULTIPLES OF 4 FROM 11 TO 50")
e = range(12,50,4)
for x in e:
    print(x) 
else:
    print("THE LOOP IS COMPLETED") 

# IF USING for LOOP ALONG WITH break STATEMENT THEN else STATEMENT WILL BECOME GARBAGE .

f = range(17)
for x in f:
    if x == 9:
        break
    print(x)
else:
    print ("THE LOOP IS FINISHED")   
    
# NESTED for LOOP : IT IS for LOOP INSIDE for LOOP .

# EXAMPLE ONE

g = [ "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" , "SEVEN" , "EIGHT" ]
h = [ "MANGO" , "BANANA" , "ORANGE" , "APPLE" , "KIWI" , "GUAVA" ] 

for x in g:
    for y in h:
        print(x,y)

# EXAMPLE TWO       

g = [ "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" , "SEVEN" , "EIGHT" ]
h = [ "MANGO" , "BANANA" , "ORANGE" , "APPLE" , "KIWI" , "GUAVA" ] 
k = [ "SMALL" , "MEDIUM" , "BIG" ]

for x in g:
    for y in k:
        for z in h:
            print(x,y,z)        

# THE pass STATEMENT .

m = [1,2,3,4,5,6,7,8]
for x in m:
    pass