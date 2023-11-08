# CREATE A PARENT CLASS .

class person:

    def __init__ ( self , firstname , lastname , age , country ) :
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country

    def fullname ( self ) : 
        print ( "MY FULL NAME IS" , self.firstname , self.lastname )  

p1 = person ( "JUSTIN" , "BIEBER" , 48 , "IRELAND" ) 
p1.fullname()

p2 = person ( "TOM" , "CRUISE" , 36 , "SCOTLAND" )
p2.fullname()

p3 = person ( "ALAN" , "WALKER" , 60 , "ENGLAND" )
p3.fullname()

p4  = person ( "JOE" , "BIDEN" , 76 , "AMERICA" )
p4.fullname()

# CREATE A CHILD CLASS . 

class student(person):

    def details ( self ) :
        print ( "THE NATIVE COUNTRY OF STUDENT IS" , self.country , "AND STUDENT AGE IS" , self.age )

s1 = student ( "VIRAT" , "KOHLI" , 40 , "CANADA" )
s1.fullname()
s1.details()

s2 = student ( "ROHIT" , "SHARMA" , 44 , "AUSTRALIA" )
s2.fullname()
s2.details()

s3 = student ( "KULDEEP" , "YADAV" , 56 , "ICELAND" )
s3.fullname()
s3.details()

s4 = student ( "SHUBMAN" , "GILL" , 70 , "NEWZEALAND" )
s4.fullname()
s4.details()

# ADD __init__ FUNCTION TO CHILD CLASS .

class sportsperson:

    def __init__  ( self , firstname , lastname ) :
        self.firstname = firstname
        self.lastname = lastname

    def completename ( self ) :
        print ( "THE FULL NAME IS" , self.firstname , self.lastname ) 

class cricketer(sportsperson):

    def __init__ ( self , firstname , lastname ) :
        sportsperson. __init__ ( self , firstname , lastname ) 

c1 = cricketer ( "VIRAT" , "KOHLI" ) 
c1.completename()

c2 = cricketer ( "ROHIT" , "SHARMA" ) 
c2.completename()

c3 = cricketer ( "KULDEEP" , "YADAV" )
c3.completename()

c4 = cricketer ( "SHUBMAN" , "GILL" )
c4.completename()

# ADD pass STATEMENT TO CHILD CLASS .

class sportsperson:

    def __init__  ( self , firstname , lastname ) :
        self.firstname = firstname
        self.lastname = lastname

    def completename ( self ) :
        print ( "MY FULL NAME IS" , self.firstname , self.lastname ) 

class cricketer(sportsperson):
    pass

c1 = cricketer ( "VIRAT" , "KOHLI" ) 
c1.completename()

c2 = cricketer ( "ROHIT" , "SHARMA" ) 
c2.completename()

c3 = cricketer ( "KULDEEP" , "YADAV" )
c3.completename()

c4 = cricketer ( "SHUBMAN" , "GILL" )
c4.completename()

# ADD super() FUNCTION TO CHILD CLASS .

class sportsperson:

    def __init__ ( self , firstname , lastname ) :
        self.firstname = firstname
        self.lastname = lastname

    def completename ( self ) :
        print ( "MY FULL NAME IS" , self.firstname , self.lastname ) 

class cricketer(sportsperson):

    def __init__ ( self , firstname , lastname ) :
        super(). __init__ ( firstname , lastname ) 

c1 = cricketer ( "VIRAT" , "KOHLI" ) 
c1.completename()

c2 = cricketer ( "ROHIT" , "SHARMA" ) 
c2.completename()

c3 = cricketer ( "KULDEEP" , "YADAV" )
c3.completename()

c4 = cricketer ( "SHUBMAN" , "GILL" )
c4.completename()  

# ADD PROPERTIES TO CHILD CLASS .

class sportsperson:

    def __init__ ( self , firstname , lastname ) :
        self.firstname = firstname
        self.lastname = lastname

    def personname ( self ) :
        print ( "MY FULL NAME IS" , self.firstname , self.lastname ) 

class cricketer(sportsperson):

    def __init__ ( self , firstname , lastname , birthyear , city ) :
        super(). __init__ ( firstname , lastname )  
        self.birthyear = birthyear
        self.city = city
        self.nationality = "INDIAN" 

    def getinfo ( self ) :
        print ( "THE BIRTH YEAR :" , self.birthyear , "AND THE CITY :" , self.city )

c1 = cricketer( "VIRAT" , "KOHLI" , 1988 , "RAIPUR" )
c1.personname()
c1.getinfo() 
print ( c1.nationality ) 
print ( c1.city )   

c2 = cricketer( "ROHIT" , "SHARMA" , 1984 , "JAIPUR" )
c2.personname()
c2.getinfo() 
print ( c2.nationality )  
print ( c2.city )   

c3 = cricketer ( "KULDEEP" , "YADAV" , 1980 , "KANPUR" )
c3.personname()
c3.getinfo() 
print ( c3.nationality )
print ( c3.city )     

c4 = cricketer ( "SHUBMAN" , "GILL" , 1976 , "NAGPUR" )
c4.personname()
c4.getinfo()  
print ( c4.nationality )
print ( c4.city )    