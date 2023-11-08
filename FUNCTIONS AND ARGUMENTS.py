# FUNCTIONS ARE BASICALLY A BLOCK OF CODE .

# CREATE AND CALL A FUNCTION .

def print_func ():
    print ("PYTHON IS HIGH LEVEL OBJECT ORIENTED PROGRAMMING LANGUAGE")

print_func() 

# ARGUMENTS ARE SPECIFIED AFTER THE FUNCTION NAME INSIDE THE PARENTHESES .

# IN SINGLE FUNCTION MULTIPLE ARGUMENTS ALSO KNOWN AS args CAN BE GIVEN TO IT .

# FUNCTION WITH ONE ARGUMENT .

def age_func (age) :
    print ( "MY AGE IS" + " " + age )

age_func("36")
age_func("THIRTY SIX")    

# FUNCTION WITH TWO ARGUMENTS .

def fullname_func ( firstname , lastname ) :
    print ( "MY FULL NAME IS" , firstname , lastname )

fullname_func ( "JUSTIN" , "BIEBER" ) 
fullname_func ( "ALAN" , "WALKER" )
fullname_func ( "JOE" , "BIDEN" )

# ARBITRARY ARGUMENT ALSO KNOWN AS *args .

def number_func (*nums) :
    print ( "THE SMALLEST NUMBER IN THE LIST OF NUMBERS :" , nums[4] , "THE LARGESTEST NUMBER IN THE LIST OF NUMBERS :" , nums[3] )

number_func ( "36" , "28" , "40" , "48" , "24" , "44" , "32" )    

# KEYWORDS ARGUMENTS . 

def integer_func ( int1 , int2 , int3 , int4 , int5 ) :
    print ( "THE LARGEST INTEGER :" , int3 , "THE SMALLEST INTEGER :" , int4 )

integer_func ( int2="16" , int5="18" , int4="12" , int3="20" , int1="14" )

# ARBITRARY KEYWORDS ARGUMNETS ALSO KNOWN AS **kwargs .

def country_func (**countries) :
    print ( "THE HAPPIEST COUNTRY IN THE WORLD IS" , countries["country4"] )

country_func( country1="DENAMRK" , country2="SWEDEN" , country3="FINLAND" , country4="NORWAY" , country5="IRELAND" , country6="AUSTRIA" )    

# DEFAULT PARAMETER VALUE .

def colour_func ( colour="BLUE" ) :
    print ( "MY FAVOURITE COLOR IS " + colour )

colour_func("ORANGE")
colour_func("GREEN")
colour_func("VIOLET")
colour_func()
colour_func("YELLOW")
colour_func("BROWN")

# PASSING LIST AS AN ARGUMENT .

def list_func (arguments) :
    for x in arguments:
        print(x)

fruits = [ "MANGO" , "BANANA" , "KIWI" , "ORANGE" , "GUAVA" , "APPLE" ]
list_func(fruits)

metals = [ "SODIUM" , "POTASSIUM" , "MAGNESIUM" , "CALCIUM" , "LITHIUM" , "ALUMINIUM" ]
list_func(metals)

# TO LET A FUNCTION GET A VALUE THEN return STATEMENT IS USED .

# EXAMPLE ONE 

def return_func ( firstname , lastname ) :
    return "MY FULL NAME IS" + " " + firstname + " " + lastname 

print ( return_func ( "TOM" , "CRUISE" ) )

# EXAMPLE TWO

def product_func ( value1 , value2 ) :
    valueproduct = value1 * value2 
    return valueproduct

print ( product_func ( 12 , 16 ) )
print ( product_func ( 24 , 20 ) )
print ( product_func ( 6 , 8 ) )
print ( product_func ( 18 , 30 ) )

# EXAMPLE THREE

def plus_func ( num1 , num2 , num3=16 ) :
    numtotal =  num1 + num2 + num3 
    return numtotal

print ( plus_func ( 18 , 12 , 20 ) )
print ( plus_func ( 24 , 36 , 8 ) )
print ( plus_func ( 18 , 12 ) ) 
print ( plus_func ( 24 , 36 ) )

# THE pass STATEMENT .

# EXAMPLE ONE 

def minus_func () :
    pass

# EXAMPLE TWO

def minus_func ( fig1 , fig2 ) :
    pass

# EXAMPLE THREE

def minus_func ( fig1 , fig2 ) :
    return fig1 - fig2
    pass