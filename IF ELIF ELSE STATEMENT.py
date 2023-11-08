'''
PYTHON CONDITIONS IN if STATEMENT :
x == y i.e. x is equal to y 
x < y i.e. x is less than y
x > y i.e. x is greater than y
x <= y i.e. x is less than or equal to y
x >= y i.e. x is greater than or equal to y
x != y i.e. x is not equal to y 
'''

# EXAMPLE OF if else STATEMENT .

a = 64
b = 36

if a < b :
    print ("VALUE OF A < VALUE OF B")
else:
    print ("VALUE OF A > VALUE OF B")

# elif STATEMENT IS USED WHEN THE PREVIOUS STATEMENT IS NOT TRUE THAN  TRY NEW STATEMENT .

# c = float ( input ( "ENTER THE FIRST FLOATING NUMBER :" ) )
# d = float ( input ( "ENTER THE SECOND FLOATING NUMBER :" ) )

c = 48
d = 40

if c < d :
    print ("VALUE OF C < VALUE OF D")
elif c > d :
    print ("VALUE OF C > VALUE OF D")   
else:
    print ("VALUE OF C == VALUE OF D")  

# else STATEMENT IS USED WHEN ANY OF PREVIOUS STATEMENT IS NOT TRUE .

# else STATEMENT CAN ALSO BE USED WITHOUT elif STATEMENT .

# EXAMPLE OF SINGLE LINE if STATEMENT WITH ONE CONDITION .

e = 20
f = 16
if e > f : print ("VALUE OF E < VALUE OF F")

# EXAMPLE OF SINGLE LINE if else STATEMENT WITH TWO CONDITION .

e = 20
f = 16
print ("VALUE OF E < VALUE OF F") if e > f else print ("VALUE OF E > VALUE OF F")

# EXAMPLE OF SINGLE LINE if else STATEMENT WITH THREE CONDITION .

g = 80
h = 80
print ("G > H") if g > h else print ("G < H") if g < h else print ("G == H") 

# and IS A LOGICAL OPERATOR WHICH IS USED TO COMBINE THE CONDITIONAL STATMENT .

k = 60
m = 72
n = 84

if k >= m and k >= n :
    print ("K IS GREATEST VALUE")

if m >= k and m >= n :
    print ("M IS GREATEST VALUE")    

else :
    print ("N IS GREATEST VALUE")

# or IS A LOGICAL OPERATOR WHICH IS USED TO COMBINE THE LOGICAL STATMENT .

k = 60
m = 72
n = 84

if k > m or n > m :
    print ("AT LEAST ONE CONDITION STATEMENT IS TRUE")

# NESTED if STATEMENT : IT IS if STATEMENT INSIDE if STATEMENT .

p = 56
if p > 40:
    print ("P > 40") 
    if p > 60:
        print ("P > 60")
    elif p > 40 and p < 60:
        print ("P > 40 AND P < 60")  
    else:
        print ("P == 60")
elif p < 40:
    print("P < 40")  
else:
    print("P == 40") 

# pass STATEMENT : IT IS USED WHEN if STATEMENT HAS NO CONTENT TO AVOID ERROR IN PROGRAM .

q = 92
r = 52

# EXAMPLE FIRST 

if q > r:
    pass

# EXAMPLE SECOND

if q > r:
    pass
else:
    pass

# EXAMPLE THIRD

if q > r:
    pass
elif q < r:
    pass
else:
    pass