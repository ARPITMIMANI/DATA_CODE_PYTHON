# JSON IS A SYNTAX FOR STORING AND EXCHANGING THE DATA . IT IS A TEXT WRITTEN WITH JAVASCRIPT OBJECT NOTATION .

# JSON IS A SUBSET OF JAVASCRIPT SYNTAX USED AS A LIGHT WEIGHT DATA INTERCHANGE FORMAT .

# GET THE dir OF json MODULE .

import json
print ( dir(json) )

# THE RESULT WILL BE PYTHON DICTIONARY WILL CONVERTING FROM JSON TO PYTHON .

import json
a1 = '{ "JIM":82 , "TOM":74 , "DAN":88 , "FIN":92 , "LEO":78 , "REX":84 }'
a2 = json.loads(a1)
print(a2)

# THE RESULT WILL BE STRING WILL CONVERTING FROM PYTHON TO JSON .

import json
b1 = { "INDIGO":28 , "BLUE":16 , "GREEN":12 , "YELLOW":32 , "ORANGE":24 , "BROWN":20 }
b2 = json.dumps(b1)
print(b2)

# CONVERT PYTHON LIST TO JSON .

import json
c1 = [ "SCOTLAND" , "ICELAND" , "NORWAY" , "FINLAND" , "SWEDEN" , "IRELAND" ]
c2 = json.dumps(c1)
print(c2)


# CONVERT PYTHON TUPLE TO JSON .

import json
d1 = ( "ONE" , "TWO" , "THREE" , "FOUR" , "FIVE" , "SIX" )
d2 = json.dumps(d1)
print(d2)

# CONVERT PYTHON STRING TO JSON .

import json
e1 = "GOOD MORNING"
e2 = json.dumps(e1)
print(e2)

# CONVERT PYTHON INTEGER TO JSON .

# EXAMPLE ONE 

import json
f1 = 36
f2 = json.dumps(f1)
print(f2)

# EXAMPLE TWO

import json
g1 = -128
g2 = json.dumps(g1)
print(g2)

# CONVERT PYTHON FLOAT TO JSON .

import json
h1 = 40.96
h2 = json.dumps(h1)
print(h2)

# CONVERT PYTHON BOOLEAN TO JSON .

# EXAMPLE ONE 

import json
m1 = True
m2 = json.dumps(m1)
print(m2)

# EXAMPLE TWO

import json
n1 = False
n2 = json.dumps(n1)
print(n2)

# CONVERT PYTHON NONETYPE TO JSON . 

import json
p = None
p = json.dumps(None)
print(p)
print ( type(p) )

# PYTHON SETS CANNOT BE CONVERTED TO JSON .

# WHILE CONVERTING FROM PYTHON TO JSON THE PYTHON OBJECTS ARE CONVERTED INTO JAVASCRIPT JSON .

import json

q1 = { "NAME":"WAGNOR" , "MODEL": [ "LXI" , "VXI" , "ZXI" ]  , "YEAR": 2012 , "WHEELS": 4 , "PETROL": True , "DIESEL" : False ,"MILEAGE" : 19.36 , "ELECTRIC" : None , "COLOR": ( "SILVER" , "BLUE" , "RED" , "WHITE" ) }

q2 = json.dumps(q1)
print(q2)

# indent KEYWORD IS USED TO MAKE IT EASIER TO READ BY FORMATTING IT .

import json

q1 = { "NAME":"WAGNOR" , "MODEL": [ "LXI" , "VXI" , "ZXI" ]  , "YEAR": 2012 , "WHEELS": 4 , "PETROL": True , "DIESEL" : False ,"MILEAGE" : 19.36 , "ELECTRIC" : None , "COLOR": ( "SILVER" , "BLUE" , "RED" , "WHITE" ) }

q3 = json.dumps ( q1 , indent=4 )
print(q3)

# separators KEYWORD IS USED TO DEFINE THE SEPARATORS LIKE COMMA , DOT , SEMICOLON , COLON , ASTERISK .

import json

q1 = { "NAME":"WAGNOR" , "MODEL": [ "LXI" , "VXI" , "ZXI" ]  , "YEAR": 2012 , "WHEELS": 4 , "PETROL": True , "DIESEL" : False ,"MILEAGE" : 19.36 , "ELECTRIC" : None , "COLOR": ( "SILVER" , "BLUE" , "RED" , "WHITE" ) }

q4 = json.dumps ( q1 , indent=4 , separators= ( " . " , " = " ) )
print(q4)

# sort_keys KEYWORD IS USED TO SORT THE KEYS IN ASCENDING ORDER .

import json

q1 = { "NAME":"WAGNOR" , "MODEL": [ "LXI" , "VXI" , "ZXI" ]  , "YEAR": 2012 , "WHEELS": 4 , "PETROL": True , "DIESEL" : False ,"MILEAGE" : 19.36 , "ELECTRIC" : None , "COLOR": ( "SILVER" , "BLUE" , "RED" , "WHITE" ) }

q5 = json.dumps ( q1 , indent=4 , sort_keys=True , separators= ( " . " , " = " ) )
print(q5)