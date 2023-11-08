'''
THERE ARE 7 TYPES OF OPERARTORS USED IN PYTHON ARE:
1. ARITHMETIC OPERATOR
2. ASSIGNMENT OPERATOR
3. BITWISE OPERATOR
4. COMPARISON OPERATOR
5. IDENTITY OPERATOR
6. LOGICAL OPERATOR
7. MEMBERSHIP OPERATOR 
'''

# ARITHMETIC OPERATORS 

a = 16
b = 6

print ( a + b )
print ( a * b )
print ( a - b )
print ( a / b )
print ( a % b )
print ( a // b )
print ( a ** b )

# ASSIGNMENT OPERATOR 

c = 12
print(c)

# c += 8 IS SAME AS  c = c + 8
c = 12
c += 8
print(c)  

# c *= 8 IS SAME AS  c = c * 8
c = 12
c *= 8
print(c)

# c -= 8 IS SAME AS  c = c - 8
c = 12
c -= 8
print(c)

# c /= 8 IS SAME AS  c = c / 8
c = 12
c /= 8
print(c)

# c %= 8 IS SAME AS  c = c % 8
c = 12
c %= 8
print(c)

# c //= 8 IS SAME AS  c = c // 8
c = 12
c //= 8
print(c)

# c **= 8 IS SAME AS  c = c / 8
c = 12
c **= 8
print(c)

# COMPARISON OPERATOR

d = 5
e = 3 

print ( d == e )
print ( d > e  )
print ( d < e )
print ( d >= e )
print ( d <=e )
print ( d != e )

# LOGICAL OPERATOR 

f = 40

print ( f>24 and f<72 )
print ( f>16 and f<32 )
print ( f>48 and f<84 )
print ( f>12 and f<28 )

print ( f>24 or f<72 )
print ( f>16 or f<32 )
print ( f>48 or f<84 )
print ( f>56 or f<28 )

print ( not ( f>24 and f<72 ) )
print ( not ( f>16 and f<32 ) )
print ( not ( f>48 and f<84 ) )
print ( not ( f>12 and f<28 ) )

print ( not ( f>24 or f<72 ) )
print ( not ( f>16 or f<32 ) )
print ( not ( f>48 or f<84 ) )
print ( not ( f>56 or f<28 ) )

print ( not ( f==40 ) )
print ( not ( f!=40 ) )

print ( not ( f==50 ) )
print ( not ( f!=50 ) )

# IDENTITY OPERATOR 

g = [1,2,3,4,5,6]
h = [1,2,3,4,5,6]
k = g 

print ( g is h )
print ( h is g )
# RETURN False BECAUSE "g" IS NOT THE SAME OBJECT AS "h" EVEN IF THEY HAVE THE SAME CONTENT .

print ( g is k )
print ( k is g )
# RETURN True BECAUSE "g" IS THE SAME OBJECT AS "k" .

print ( g is not h )
print ( h is not g )
# RETURN True BECAUSE "g" IS NOT THE SAME OBJECT AS "h" EVEN IF THEY HAVE THE SAME CONTENT .

print ( g is not k )
print ( k is not g )
# RETURN False BECAUSE "g" IS THE SAME OBJECT AS "k" .

# MEMBERSHIP OPERATOR 

m = [ "ONE" , "TWO" , "THREE" , "FOUR" , "FIVE" , "SIX" ]
print ( "FOUR" in m )

m = [ "ONE" , "TWO" , "THREE" , "FOUR" , "FIVE" , "SIX" ]
print ( "EIGHT" in m )

m = [ "ONE" , "TWO" , "THREE" , "FOUR" , "FIVE" , "SIX" ]
print ( "FOUR" not in m )

m = [ "ONE" , "TWO" , "THREE" , "FOUR" , "FIVE" , "SIX" ]
print ( "EIGHT" not in m )