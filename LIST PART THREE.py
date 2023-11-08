 # LOOP THROUGH LIST ITEMS USING for LOOP .

a = [ "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" ] 
for x in a:
    print(x)

# LOOP THROUGH INDEX NUMBERS USING for LOOP .  

a = [ "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" ] 

b = len(a)  
for x in range(b):
    print ( a[x] ) 

# LOOP THROUGH LIST ITEMS USING while LOOP .    

a = [ "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" ] 

x = 0
while x < len(a):
    print ( a[x] )
    x = x + 1 

# LOOP THROUGH LIST ITEMS USING for LOOP AND if STATEMENT . 

c = [ "ONE" , "TWO" , "THREE" , "FOUR" , "FIVE" , "SIX" , "SEVEN" , "EIGHT" ]

d = []
for x in c:
    if "E" in x:
        d.append(x)
print(d)  

# LOOP THROUGH LIST ITEMS USING LIST COMPREHENSION . 

c = [ "ONE" , "TWO" , "THREE" , "FOUR" , "FIVE" , "SIX" , "SEVEN" , "EIGHT" ]
[ print(x) for x in c ]

c = [ "ONE" , "TWO" , "THREE" , "FOUR" , "FIVE" , "SIX" , "SEVEN" , "EIGHT" ]
d = [ x for x in c if "E" in x ]
print(d)