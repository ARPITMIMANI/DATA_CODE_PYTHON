# DICTIONARY ARE ORDERED , CHANGEALBE BUT INDEXED .

# EXAMPLE OF A DICTIONARY .

car = { 
    "NAME":"WAGNOR" , 
    "MODEL":"LXI" , 
    "YEAR":2012 , 
    "WHEELS":4 , 
    "FUEL":"PETROL" , 
    "COLOR":"SILVER" }

print(car)
print ( type(car) )

# print() THE VALUE FROM THE DICTIONARY .

car = { 
    "NAME":"WAGNOR" , 
    "MODEL":"LXI" , 
    "YEAR":2012 , 
    "WHEELS":4 , 
    "FUEL":"PETROL" , 
    "COLOR":"SILVER" }

print ( car["MODEL"] )

# DICTIONARY DO NOT ACCEPT DUPLICATE KEYS .

new_car = { 
    "NAME":"WAGNOR" , 
    "MODEL":"LXI" , 
    "YEAR":2012 , 
    "WHEELS":4 , 
    "FUEL":"PETROL" , 
    "COLOUR":"SILVER" , 
    "COLOUR":"BLUE" }

print(new_car)

# DICTIONARY VALUES ARE ORDERED FROM PYTHON VERSION 3.7 AND HIGHER .

# DICTIONARY VALUES ARE UNORDERED FROM PYTHON VERSION 3.6 AND LOWER .

# CHECK THE LENGTH OF THE DICTIONARY .

car = { 
    "NAME":"WAGNOR" , 
    "MODEL":"LXI" , 
    "YEAR":2012 , 
    "WHEELS":4 , 
    "FUEL":"PETROL" , 
    "COLOR":"SILVER" }

print ( len(car) )

new_car = { 
    "NAME":"WAGNOR" , 
    "MODEL":"LXI" , 
    "YEAR":2012 , 
    "WHEELS":4 , 
    "FUEL":"PETROL" , 
    "COLOUR":"SILVER" , 
    "COLOUR":"BLUE" }

print ( len(new_car) )

# DICTIONARY WITH VALUES OF MIXED DATA TYPE .

# CASE 1 : LIST 

car_details = { 
    "NAME":"WAGNOR" , 
    "MODEL":"LXI" , 
    "YEAR":2012 , 
    "WHEELS":4 , 
    "FUEL":"PETROL" ,
    "TANK" : 40.96 , 
    "ROOF" : True ,
    "COLOR": [ "SILVER" , "BLUE" ,   "RED" , "WHITE" ] }

print(car_details)

# CASE 2 : TUPLE 

car_details = { 
    "NAME":"WAGNOR" , 
    "MODEL":"LXI" , 
    "YEAR":2012 , 
    "WHEELS":4 , 
    "FUEL":"PETROL" ,
    "TANK" : 40.96 , 
    "ROOF" : True ,
    "COLOR": ( "SILVER" , "BLUE" ,   "RED" , "WHITE" ) }

print(car_details)

# CASE 3 : SET

car_details = { 
    "NAME":"WAGNOR" , 
    "MODEL":"LXI" , 
    "YEAR":2012 , 
    "WHEELS":4 , 
    "FUEL":"PETROL" ,
    "TANK" : 40.96 , 
    "ROOF" : True ,
    "COLOR": { "SILVER" , "BLUE" , "RED" , "WHITE" }  }

print(car_details)

# ACCESS ITEMS OF DICTIONARY USING INDEXING METHOD .

car = { 
    "NAME":"WAGNOR" , 
    "MODEL":"LXI" , 
    "YEAR":2012 , 
    "WHEELS":4 , 
    "FUEL":"PETROL" , 
    "COLOR":"SILVER" }

a = car["FUEL"]
print(a)

# ACCESS ITEMS OF DICTIONARY USING get() METHOD .

car = { 
    "NAME":"WAGNOR" , 
    "MODEL":"LXI" , 
    "YEAR":2012 , 
    "WHEELS":4 , 
    "FUEL":"PETROL" , 
    "COLOR":"SILVER" }

b = car.get("NAME")
print(b)

# keys() IS USED TO ACCESS ALL KEY ITEMS FROM THE DICTIONARY .

# EXAMPLE ONE

car = { 
    "NAME":"WAGNOR" , 
    "MODEL":"LXI" , 
    "YEAR":2012 , 
    "WHEELS":4 , 
    "FUEL":"PETROL" , 
    "COLOR":"SILVER" }

c = car.keys()
print(c)

# EXAMPLE TWO

new_car = { 
    "NAME":"WAGNOR" , 
    "MODEL":"LXI" , 
    "YEAR":2012 , 
    "WHEELS":4 , 
    "FUEL":"PETROL" , 
    "COLOUR":"SILVER" , 
    "COLOUR":"BLUE" }

d = new_car.keys()
print(d)

# values() IS USED TO ACCESS ALL VALUE ITEMS FROM THE DICTIONARY .

# EXAMPLE ONE

car = { 
    "NAME":"WAGNOR" , 
    "MODEL":"LXI" , 
    "YEAR":2012 , 
    "WHEELS":4 , 
    "FUEL":"PETROL" , 
    "COLOR":"SILVER" }

e = car.values()
print(e)

# EXAMPLE TWO

car_details = { 
    "NAME":"WAGNOR" , 
    "MODEL":"LXI" , 
    "YEAR":2012 , 
    "WHEELS":4 , 
    "FUEL":"PETROL" ,
    "TANK" : 40.96 , 
    "ROOF" : True ,
    "COLOR": [ "SILVER" , "BLUE" ,   "RED" , "WHITE" ] }

f = car_details.values()
print(f)

# items() IS USED TO ACCESS ALL ITEMS AS TUPLES IN A LIST FROM THE DICTIONARY .

# ALL ITEMS ARE COMBINATION OF ALL KEYS AND ALL VALUES IN A DICTIONARY .

car = { 
    "NAME":"WAGNOR" , 
    "MODEL":"LXI" , 
    "YEAR":2012 , 
    "WHEELS":4 , 
    "FUEL":"PETROL" , 
    "COLOR":"SILVER" }

g = car.items()
print(g)

# ADDING " KEY AND VALUE " ITEMS TO THE DICTIONARY .

marks = {
    "JIM":82 ,
    "TOM":74 ,
    "DAN":88 ,
    "FIN":92 ,
    "LEO":78 ,
    "REX":84 
    }

print(marks)

marks["KIT"] = 72
print(marks)

# CHANGING VALUE ITEMS TO THE DICTIONARY .

marks = {
    "JIM":82 ,
    "TOM":74 ,
    "DAN":88 ,
    "FIN":92 ,
    "LEO":78 ,
    "REX":84 
    }

print(marks)

marks["FIN"] = 86
print(marks)

# CHECK IF THE KEY ITEM EXIST IN THE DICTIONARY .

marks = {
    "JIM":82 ,
    "TOM":74 ,
    "DAN":88 ,
    "FIN":92 ,
    "LEO":78 ,
    "REX":84 
    }

if "DAN" in marks:
    print("YES")
else:
    print("NO")    

if "dan" in marks:
    print("YES")
else:
    print("NO")  

print ( "DAN" in marks ) 

print ( "dan" in marks ) 