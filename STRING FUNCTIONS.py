# UPPER CASE IN STRING USING upper() .

a = "my full name is justin bieber ."
print ( a.upper() )

# LOWER CASE IN STRING USING lower() .

a = "MY FULL NAME IS JUSTIN BIEBER ."
print ( a.lower() )

# CAPITALIZE CASE IN STRING USING capitalize() .

a = "MY FULL NAME IS JUSTIN BIEBER ."
print ( a.capitalize() )

# TITLE CASE IN STRING USING title() .

a = "MY FULL NAME IS JUSTIN BIEBER ."
print ( a.title() )

# REMOVING WHITE SPACE IN STRING USING strip() .

b = " GERMANY DENMARK ITALY NORWAY SWEDEN FINLAND. "
print ( b.strip() )

# REPLACE STRING USING replace() .

b = "GERMANY DENMARK ITALY NORWAY SWEDEN FINLAND"
print ( b.replace ( "ITALY" , "POLAND" ) )

# SPLIT STRING USING split() .

b = "GERMANY , DENMARK , ITALY , NORWAY , SWEDEN , FINLAND"
print ( b.split (",") )

b = "GERMANY DENMARK ITALY NORWAY SWEDEN FINLAND"
print ( b.split (" ") )

b = "GERMANY , DENMARK , ITALY , NORWAY , SWEDEN , FINLAND"
print ( b.split (" ") )

# CONCATENATION OF STRINGS using "+" .

c = "MY"
d = "FULL"
e = "NAME" 
f = "IS"
g = "ALAN"
h = "WALKER"

k = c + d + e + f + g + h
print(k)

m = c + " " + d + " " + e + " " + f + " " +  g + " " +  h
print(m)

# CONCATENATION OF STRINGS OF SINGLE ARGUMENT WITHOUT INDEXING USING format() .

age_one = 48 
txt_one = "MY AGE IS {}"
print ( txt_one.format (age_one) )

age_two = "FOURTY EIGHT"
txt_two = "MY AGE IS {}"
print ( txt_two.format (age_two) )

# CONCATENATION OF STRINGS OF MULTIPLE ARGUMENT WITHOUT INDEXING USING format() .

quantity = 6
itemid = 1296
amount = 72
myorder = "I WANT {} PIECES OF ITEM NUMBER {} FOR PRICE {} RUPEES ."
print ( myorder.format ( quantity , itemid , amount ) )

# CONCATENATION OF STRINGS OF MULTIPLE ARGUMENT WITH INDEXING USING format() .

quantity = 6
itemid = 1296
amount = 72
myorder = "I WANT {2} PIECES OF ITEM NUMBER {0} FOR PRICE {1} RUPEES ."
print ( myorder.format ( itemid , amount , quantity ) )