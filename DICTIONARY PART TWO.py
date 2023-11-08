# CHANGING VALUES OF THE DICTIONARY USING update() FUNCTION .

car = { 
    "NAME":"WAGNOR" , 
    "MODEL":"LXI" , 
    "YEAR":2012 , 
    "WHEELS":4 , 
    "FUEL":"PETROL" , 
    "COLOR":"SILVER" }

car.update ({ "FUEL":"CNG" })
print(car)

# ADDING ITEMS TO THE DICTIONARY USING update() FUNCTION .

car = { 
    "NAME":"WAGNOR" , 
    "MODEL":"LXI" , 
    "YEAR":2012 , 
    "WHEELS":4 , 
    "FUEL":"PETROL" , 
    "COLOR":"SILVER" }

car.update ({ "WEIGHT":1936 , "TOPSPEED":160 })
print(car)

# CHANGING VALUES AND ADDING ITEMS TOGETHER IN THE DICTIONARY USING update() FUNCTION .

car = { 
    "NAME":"WAGNOR" , 
    "MODEL":"LXI" , 
    "YEAR":2012 , 
    "WHEELS":4 , 
    "FUEL":"PETROL" , 
    "COLOR":"SILVER" }

car.update ({ "FUEL":"CNG" , "WEIGHT":1936 })
print(car)

# pop() FUNCTION IS USED TO REMOVE ITEMS FROM THE DICTIONARY .

marks = {
    "JIM":82 ,
    "TOM":74 ,
    "DAN":88 ,
    "FIN":92 ,
    "LEO":78 ,
    "REX":84 
    }

marks.pop("TOM")
print(marks)

# popitem() FUNCTION IS USED TO REMOVE LAST ITEM FROM THE DICTIONARY .

marks = {
    "JIM":82 ,
    "TOM":74 ,
    "DAN":88 ,
    "FIN":92 ,
    "LEO":78 ,
    "REX":84 
    }

marks.popitem()
print(marks)

# del KEYWORD IS USED TO REMOVE THE ITEMS WITH THE SPECIFIC KEY NAME .

marks = {
    "JIM":82 ,
    "TOM":74 ,
    "DAN":88 ,
    "FIN":92 ,
    "LEO":78 ,
    "REX":84 
    }

del marks["DAN"]
print(marks)

# del KEYWORD IS USED TO COMPLETELY DELETE THE WHOLE DICTIONARY .

marks = {
    "JIM":82 ,
    "TOM":74 ,
    "DAN":88 ,
    "FIN":92 ,
    "LEO":78 ,
    "REX":84 
    }

del marks

# clear() FUNCTION IS USED TO EMPTY THE DICTIONARY .

marks = {
    "JIM":82 ,
    "TOM":74 ,
    "DAN":88 ,
    "FIN":92 ,
    "LEO":78 ,
    "REX":84 
    }

marks.clear()
print(marks)