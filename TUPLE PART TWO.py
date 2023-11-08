 # LOOP THROUGH TUPLE ITEMS USING for LOOP .

a = ( "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" )
for x in a:
    print(x)

# LOOP THROUGH INDEX NUMBERS USING for LOOP .  

a = ( "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" )

b = len(a) 
for x in range(b):
    print ( a[x] )  

# LOOP THROUGH LIST ITEMS USING while LOOP .    

a = ( "GERMANY" , "DENMARK" , "NORWAY" , "SWEDEN" , "FINLAND" , "POLAND" , "BELGIUM" , "AUSTRIA" )

c = 0
while c < len(a):
    print ( a[c] )
    c = c + 1