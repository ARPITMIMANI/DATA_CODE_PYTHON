# PYTHON HAS TWO PRIMITIVE LOOPS THEY ARE WILE LOOP AND FOR LOOP .

# EXAMPLE OF WHILE LOOP .

# PRINT ALL NUMBERS MULTIPLE OF 100 FROM 100 TO 1000 .

a = 100
while a <= 1000 :
    print(a)
    a = a + 100

# PRINT ALL EVEN NATURAL NUMBERS FROM 11 TO 30 .

b = 10
while b <= 30 :
    print(b)
    b = b + 2

# PRINT ALL NATURAL NUMBERS FROM 120 TO 111  .  

c = 120
while c >= 111 :
    print(c)
    c = c - 1

# break STATEMENT IS USED TO STOP THE LOOP .

# PRINT ALL NATURAL NUMBERS FROM 1 TO 10 BUT STOP AT NUMBER 6 . 
 
d = 1
while d <= 10 :
    print(d)
    if d == 6 :
        break
    d = d + 1

# continue STATEMENT IS USED TO SKIP THE LOOP .

# PRINT ALL NATURAL NUMBERS FROM 1 TO 10 BUT SKIP THE NUMBER 6 . 

e = 0
while e < 10 :
    e = e + 1
    if e == 6 :
        continue
    print(e)

# THE else STATEMENT .

f = 2401
while f <= 2410:
    print(f)
    f = f + 1
else:
    print ("LOOP IS COMPLETED") 