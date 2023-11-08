# CREATE A CLASS 

class democlass():
    a = 16
    b = 20

print ( democlass ) 

# CREATE A OBJECT .

class numclass():
    c = 24
    d = 28
    e = 32
    f = c + d + e

obj = numclass()

print ( obj.c )
print ( obj.d )
print ( obj.e )
print ( obj.f )

# THE __init__ FUNCTION .

class person:

    def __init__ ( self , name , age , country ) :
        self.name = name
        self.age = age
        self.country = country

p1 = person ( "JUSTIN" , 36 , "ENGLAND" ) 
p2 = person ( "TOM" , 64 , "AUSTRALIA" )
p3 = person ( "JOE" , 80 , "CANADA" )
p4 = person ( "ALAN" , 48 , "IRELAND" )

print ( p1.name , p1.age , p1.country )
print ( p2.name , p2.age , p2.country )
print ( p3.name , p3.age , p3.country )
print ( p4.name , p4.age , p4.country )

# OBJECT METHODS .

class countries:
     
     def __init__ ( self , naam , code , gdp_rank ) :
         self.naam = naam
         self.code = code
         self.gdp_rank = gdp_rank

     def native (self) :
         print ( "MY NATIVE COUNTRY IS" , self.naam )

c1 = countries ( "ITALY" , 39 , 8 )
c2 = countries ( "FRANCE" , 33 , 7 )
c3 = countries ( "ENGLAND" , 44 , 6 )
c4 = countries ( "INDIA" , 91 , 5 )
c5 = countries ( "GERMANY" , 49 , 4 )
c6 = countries ( "JAPAN" , 81 , 3 )

c1.native()
c2.native()
c3.native()
c4.native()
c5.native()
c6.native()

print ( c1.naam , c1.code , c1.gdp_rank )
print ( c2.naam , c2.code , c2.gdp_rank )
print ( c3.naam , c3.code , c3.gdp_rank )
print ( c4.naam , c4.code , c4.gdp_rank )
print ( c5.naam , c5.code , c5.gdp_rank )
print ( c6.naam , c6.code , c6.gdp_rank )

# THE self PARAMETER .

class countries:

    def __init__ ( myobject , naam , code , gdp_rank ) :
        myobject.naam = naam
        myobject.code = code
        myobject.gdp_rank = gdp_rank

    def mystate (abcdef) :
        print ( "MY NATIVE COUNTRY IS" , abcdef.naam )  

c1 = countries ( "ITALY" , 39 , 8 )
c2 = countries ( "FRANCE" , 33 , 7 )
c3 = countries ( "ENGLAND" , 44 , 6 )
c4 = countries ( "INDIA" , 91 , 5 )
c5 = countries ( "GERMANY" , 49 , 4 )
c6 = countries ( "JAPAN" , 81 , 3 )   

c1.mystate()
c2.mystate()
c3.mystate()
c4.mystate()
c5.mystate()
c6.mystate()

print ( c1.naam , c1.code , c1.gdp_rank )
print ( c2.naam , c2.code , c2.gdp_rank )
print ( c3.naam , c3.code , c3.gdp_rank )
print ( c4.naam , c4.code , c4.gdp_rank )
print ( c5.naam , c5.code , c5.gdp_rank )
print ( c6.naam , c6.code , c6.gdp_rank )

# MODIFY OBJECT PROPERTIES .

class person:

    def __init__ ( self , name , age , country ) :
        self.name = name
        self.age = age
        self.country = country

    def myidentity (self) :
        print ( "MY NAME IS" , self.name )    

p1 = person ( "JUSTIN" , 36 , "ENGLAND" ) 
p2 = person ( "TOM" , 64 , "AUSTRALIA" )
p3 = person ( "JOE" , 80 , "CANADA" )
p4 = person ( "ALAN" , 48 , "IRELAND" )

p1.myidentity()
p2.myidentity()
p3.myidentity()
p4.myidentity()

p1.age = 38
p2.age = 66
p3.age = 82
p4.age = 50

print ( p1.name , p1.age , p1.country )
print ( p2.name , p2.age , p2.country )
print ( p3.name , p3.age , p3.country )
print ( p4.name , p4.age , p4.country )

# DELETE OBJECT PROPERTIES .

class person:

    def __init__ ( self , name , age , country ) :
        self.name = name
        self.age = age
        self.country = country

    def myidentity (self) :
        print ( "MY NAME IS" , self.name )    

p1 = person ( "JUSTIN" , 36 , "ENGLAND" ) 
p2 = person ( "TOM" , 64 , "AUSTRALIA" )
p3 = person ( "JOE" , 80 , "CANADA" )
p4 = person ( "ALAN" , 48 , "IRELAND" )

del p1.country 
del p2.country
del p3.country
del p4.country

print ( p1.name , p1.age )
print ( p2.name , p2.age )
print ( p3.name , p3.age )
print ( p4.name , p4.age )

# DELETE COMPLETE OBJECT .

class person:

    def __init__ ( self , name , age , country ) :
        self.name = name
        self.age = age
        self.country = country

    def myidentity (self) :
        print ( "MY NAME IS" , self.name )    

p1 = person ( "JUSTIN" , 36 , "ENGLAND" ) 
p2 = person ( "TOM" , 64 , "AUSTRALIA" )
p3 = person ( "JOE" , 80 , "CANADA" )
p4 = person ( "ALAN" , 48 , "IRELAND" )

del p1
del p2
del p3
del p4

# THE pass STATEMENT .

class newperson:
    pass