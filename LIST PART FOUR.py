# sort() THE LIST APLHABETICALLY IN ASCENDING ORDER .

a = [ "ONE" , "TWO" , "THREE" , "FOUR" , "FIVE" , "SIX" , "SEVEN" , "EIGHT" ]
a.sort()
print(a)

# sort() THE LIST APLHABETICALLY IN DESCENDING ORDER .

a = [ "ONE" , "TWO" , "THREE" , "FOUR" , "FIVE" , "SIX" , "SEVEN" , "EIGHT" ]
a.sort ( reverse=True )
print(a)

# sort() THE LIST NUMERICALLY IN ASCENDING ORDER .

b = [34,37,32,39,35,38,33,40,31,36]
b.sort()
print(b)

# sort() THE LIST NUMERICALLY IN DESCENDING ORDER .

b = [34,37,32,39,35,38,33,40,31,36]
b.sort ( reverse=True )
print(b)

# CUSTOMIZE sort() FUNCTION .

def sort_func(x):
    return abs(x-100)

c = [128,84,108,120,88,64,144,96]
c.sort ( key=sort_func )
print(c)

# reverse() THE APLHABETICAL LIST .

a = [ "ONE" , "TWO" , "THREE" , "FOUR" , "FIVE" , "SIX" , "SEVEN" , "EIGHT" ]
a.reverse()
print(a)

# reverse() THE NUMERICAL LIST .

b = [34,37,32,39,35,38,33,40,31,36]
b.reverse()
print(b)

# COPY THE LIST USING FUNCTION copy() .

a = [ "ONE" , "TWO" , "THREE" , "FOUR" , "FIVE" , "SIX" , "SEVEN" , "EIGHT" ]
c = a.copy()
print(c)

# COPY THE LIST USING BUILD IN METHOD list() .

a = [ "ONE" , "TWO" , "THREE" , "FOUR" , "FIVE" , "SIX" , "SEVEN" , "EIGHT" ]
d = list(a)
print(d)

# JOIN THE LIST USING "+" .

a = [ "ONE" , "TWO" , "THREE" , "FOUR" , "FIVE" , "SIX" , "SEVEN" , "EIGHT" ]
b = [34,37,32,39,35,38,33,40,31,36]
e =  a + b
print(e)

# JOIN THE LIST USING extend() .

a = [ "ONE" , "TWO" , "THREE" , "FOUR" , "FIVE" , "SIX" , "SEVEN" , "EIGHT" ]
b = [34,37,32,39,35,38,33,40,31,36]
a.extend(b)
print(a)

# JOIN THE LIST USING append() .

a = [ "ONE" , "TWO" , "THREE" , "FOUR" , "FIVE" , "SIX" , "SEVEN" , "EIGHT" ]
b = [34,37,32,39,35,38,33,40,31,36]

for x in b:
    a.append(x)
print(a) 