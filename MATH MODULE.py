# GET THE dir OF math MODULE .

import math
print ( dir(math) )

# GET THE max VALUE OF THE GROUP OF NUMBERS .

a = max ( 24,32,16,36,8,12,40,4,28,20 )
print ( "THE MINIMUM VALUE IS" , a )

# GET THE min VALUE OF THE GROUP OF NUMBERS .

b  = min ( 24,32,16,36,8,12,40,4,28,20 )
print ( "THE MAXIMUM VALUE IS" , b )

# abs FUNCTION RETURNS ABSOLUTE POSITIVE VALUE .

d = abs (-77.44)
print ( "THE ABSOLUTE VALUE IS" , d )

e = abs (60.84)
print ( "THE ABSOLUTE VALUE IS" , e )

# pow FUNCTION RETURNS THE VALUE OF FIRST NUMBER TO THE POWER OF SECOND NUMBER .

f = pow (4,3)
print ( "4 ** 3 =" , f )

g = pow ( 6.4 , 3.2 )
print( "6.4 ** 3.2 =" , g )

# math MODULE CAN ALSO BE IMPORTED EXTERNALLY .

# GET THE sqrt OF THE NUMBER .

import math
h = math.sqrt(256)
print("THE SQUARE ROOT OF THE NUMBER IS" , h )

# GET THE log10 OF THE NUMBER .

import math
k = math.log10(1000)
print ( "THE LOG TO THE BASE 10 OF THE NUMBER IS" , k )

# GET THE log2 OF THE NUMBER .

import math
m = math.log2(64)
print ( "THE LOG TO THE BASE 2 OF THE NUMBER IS" , m )

# GET THE log OF THE NUMBER .

import math
n = math.log (1024,4)
print ( "THE LOG TO THE BASE 4 OF THE NUMBER IS" , n )

# IF SECOND ARGUMENT IS NOT SPECIFIED FOR log FUNCTION THEN THE DEFAULT BASE IS "e" VALUE .

# GET THE factorial OF THE NUMBER .

import math
p = math.factorial(8)
print ( "THE FACORIAL OF THE NUMBER IS" , p )

# GET THE lcm OF THE GROUP OF NUMBERS .

import math
q = math.lcm ( 32,40,48 )
print ("THE LCM OF GROUP OF NUMBER IS", q )

# GET THE gcd OF THE GROUP OF NUMBERS .

import math
r = math.gcd ( 32,40,48 )
print ("THE HCF OF GROUP OF NUMBER IS", r )

# ceil FUNCTION RETURNS THE SMALLEST INTEGER VALUE WHICH IS GREATER THAN OR EQUAL TO THE SPECIFIED NUMBER .

s1 = math.ceil(5.76)
print ( "THE CEIL VALUE OF THE NUMBER IS" , s1 )

s2 = math.ceil(-5.76)
print ( "THE CEIL VALUE OF THE NUMBER IS" , s2 )

s3 = math.ceil(3.24)
print ( "THE CEIL VALUE OF THE NUMBER IS" , s3 )

s4 = math.ceil(-3.24)
print ( "THE CEIL VALUE OF THE NUMBER IS" , s4 )

# floor FUNCTION RETURNS THE LARGEST INTEGER VALUE WHICH IS LESS THAN OR EQUAL TO THE SPECIFIFED NUMBER .

t1 = math.floor (5.76)
print ( "THE FLOOR VALUE OF THE NUMBER IS" , t1 )

t2 = math.floor (-5.76)
print ( "THE FLOOR VALUE OF THE NUMBER IS" , t2 )

t3 = math.floor (3.24)
print ( "THE FLOOR VALUE OF THE NUMBER IS" , t3 )

t4 = math.floor (-5.76)
print ( "THE FLOOR VALUE OF THE NUMBER IS" , t4 )

# GET THE hypot OF THE GROUP OF  NUMBERS .

u = math.hypot (8,6)
print( "THE HYPOTENUSE OF 12 , 5 IS" , u )

v = math.hypot (2,3,6)
print( "THE HYPOTENUSE OF 2 , 3 , 6 IS" , v )

# GET THE VALUE OF pi .

w = math.pi
print ( "THE VALUE OF pi IS" , w )