# ARRAYS ARE USED TO STORE MULTIPLE VALUES IN SINGLE VARIABLE .

# EXAMPLE OF ARRAY .

countries = [ "IRELAND" ,  "FINLAND" , "NORWAY" , "SWEDEN" , "DENMARK" , "WALES" , "ICELAND" , "SCOTLAND" , "ENGLAND" , "GREENLAND" ]  
print(countries)

# LENGTH OF AN ARRAY .

countries = [ "IRELAND" ,  "FINLAND" , "NORWAY" , "SWEDEN" , "DENMARK" , "WALES" , "ICELAND" , "SCOTLAND" , "ENGLAND" , "GREENLAND" ]  
print ( len(countries) )

# ACCESS THE ELEMENTS OF AN ARRAY .

countries = [ "IRELAND" ,  "FINLAND" , "NORWAY" , "SWEDEN" , "DENMARK" , "WALES" , "ICELAND" , "SCOTLAND" , "ENGLAND" , "GREENLAND" ]

print ( countries[3] )
print ( countries[-4] )

# MODIFY THE ELEMENTS OF AN ARRAY .

countries = [ "IRELAND" ,  "FINLAND" , "NORWAY" , "SWEDEN" , "DENMARK" , "WALES" , "ICELAND" , "SCOTLAND" , "ENGLAND" , "GREENLAND" ]
countries[3] = "MEXICO"
countries[-4] = "BRAZIL"
print(countries)

# ADDING THE ELEMENTS TO THE ARRAY .

countries = [ "IRELAND" ,  "FINLAND" , "NORWAY" , "SWEDEN" , "DENMARK" , "WALES" , "ICELAND" , "SCOTLAND" , "ENGLAND" , "GREENLAND" ]
countries.append ( "MEXICO" )
print(countries)

countries = [ "IRELAND" ,  "FINLAND" , "NORWAY" , "SWEDEN" , "DENMARK" , "WALES" , "ICELAND" , "SCOTLAND" , "ENGLAND" , "GREENLAND" ]
countries.insert ( 5 , "BRAZIL" )
print(countries)

# REMOVING THE ELEMENTS FROM THE ARRAY .

countries = [ "IRELAND" ,  "FINLAND" , "NORWAY" , "SWEDEN" , "DENMARK" , "WALES" , "ICELAND" , "SCOTLAND" , "ENGLAND" , "GREENLAND" ]
countries.remove ( "WALES" )
print(countries)

countries = [ "IRELAND" ,  "FINLAND" , "NORWAY" , "SWEDEN" , "DENMARK" , "WALES" , "ICELAND" , "SCOTLAND" , "ENGLAND" , "GREENLAND" ]
countries.pop ( 2 )
print(countries)

countries = [ "IRELAND" ,  "FINLAND" , "NORWAY" , "SWEDEN" , "DENMARK" , "WALES" , "ICELAND" , "SCOTLAND" , "ENGLAND" , "GREENLAND" ]
countries.pop ()
print(countries)

# LOOPING THROUGH THE ELEMENTS OF AN ARRAY .

countries = [ "IRELAND" ,  "FINLAND" , "NORWAY" , "SWEDEN" , "DENMARK" , "WALES" , "ICELAND" , "SCOTLAND" , "ENGLAND" , "GREENLAND" ]
for nation in countries:
    print(nation)