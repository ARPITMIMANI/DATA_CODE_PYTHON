'''

LIST OF BUILD IN DATA TYPES .

1. TEXT TYPE : str
2. NUMERIC TYPE : int , float , complex
3. SEQUENCE TYPE : list , tuple , range
4. MAPPING TYPE : dict
5. SET TYPE : set , frozenset
6. BOOLEAN TYPE : bool
7. BINARY TYPE : bytes , bytearray , memoryview  

'''
# EXAMPLES OF DATA TYPES .

a = "GOLDEN"
b = 64
c = 51.84
d = 8 + 6j
e =  [ "GREEN" , "BLUE" , "ORANGE" , "YELLOW" , "RED" , "BROWN" ]
f  = ( "GREEN" , "BLUE" , "ORANGE" , "YELLOW" , "RED" , "BROWN" )
g = range(1,11)
h = { "ENGLISH" : 72 , "SCIENCE" : 88 , "HINDI" : 68 , "MATHS" : 84 , "GEOGRAPHY" : 76 , "HISTORY" : 80 }
k = { "GREEN" , "BLUE" , "ORANGE" , "YELLOW" , "RED" , "BROWN" }
m = True
n = b"GOLDEN"
p = bytearray(10)
q = memoryview(bytes(12))

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(k)
print(m)
print(n)
print(p)
print(q)

# CHECK THE DATA TYPES OF VARIABLES .

print ( type(a) )
print ( type(b) )
print ( type(c) )
print ( type(d) )
print ( type(e) )
print ( type(f) )
print ( type(g) )
print ( type(h) )
print ( type(k) )
print ( type(m) )
print ( type(n) )
print ( type(p) )
print ( type(q) )

# SETTING THE DATA TYPES OF THE VARIABLES .

r11 = str("PLATINUM")
print(r11)

r12 = int(256)
print(r12)

r13 = float(17.42)
print(r13)

r14 = complex(5j+12)
print(r14)

r15 = list (( "ASIA" , "EUROPE" , "AMERICA" , "AFRICA" , "OCEANIA" , "ZEALANDIA" ))
print(r15)

r16 = tuple (( "ASIA" , "EUROPE" , "AMERICA" , "AFRICA" , "OCEANIA" , "ZEALANDIA" ))
print(r16)

r17 = range(21,31)
print(r17)

r18 = dict ( TOM=72 , JOE=88 , NEO=68 , DAX=84 , MAC=76 , ASH=80 )
print(r18)

r19 = set (( "ASIA" , "EUROPE" , "AMERICA" , "AFRICA" , "OCEANIA" , "ZEALANDIA" ))
print(r19)

r20 = frozenset (( "ASIA" , "EUROPE" , "AMERICA" , "AFRICA" , "OCEANIA" , "ZEALANDIA" ))
print(r20)

r21 = bool(18)
print(r21)

r22 = bytes(7)
print(r22) 

r23 = bytearray(5)
print(r23)

r24 = memoryview(bytes(32))
print(r24)