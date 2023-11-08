# EXAMPLE ONE

a1 = 64
a2 = 0

try:
    a3 = a1 / a2
except Exception as e:
    print ( "EXCEPTION OCCURED :" , e )
    a3 = None

print ( "THE OUPUT IS :" , a3 )      

# EXAMPLE TWO

b1 = 48
b2 = 0

try:
    b3 = b1 / b2
except ZeroDivisionError as z:
    print ( "EXCEPTION OCCURED :" , z )
    b3 = None

print ( "THE OUPUT IS :" , b3 )

# EXAMPLE THREE

c1 = 120
c2 = 25

try:
    c3 = c1 / c2
except Exception as e:
    print ( "EXCEPTION OCCURED :" , e )
    c3 = None

print ( "THE OUTPUT IS :" , c3 ) 

# EXAMPLE FOUR

d1 = 64
d2 = 5

try:
    d3 = d1 / d2
except ZeroDivisionError as z:
    print ( "EXCEPTION OCCURED :" , z )  
    d3 = None

print ( "THE OUTPUT IS :" , d3 )  

# EXAMPLE FIVE

e1 = "1296"
e2 = 16

try:
    e3 = e1 / e2
except ZeroDivisionError as e:
    print ( "DIVSION BY ZERO ERROR" )
    e3 = None
except Exception as e:
    print ( "THE TYPE OF ERROR IS :" , type(e).__name__ )
    e3 = None

print ( "THE OUTPUT IS :" , e3 )

# EXAMPLE SIX

f1 = "576"
f2 = 8

try:
    f3 = f1 / f2
except ZeroDivisionError as z:
    print ( "ZERO DIVISION ERROR" )
    f3 = None
except TypeError as t:
    print ( "TYPE ERROR" )
    f3 = None

print ( "THE OUTPUT IS :" , f3 )