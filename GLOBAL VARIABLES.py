# GLOBAL VARIABLE : IT IS A VARIABLE CREATED OUTSIDE A FUNCTION .

x = "ALAN WALKER"

def first_func():
    print ( "MY FULL NAME IS " + x )

first_func() 

# LOCAL VARIABLE : IT IS A VARIABLE CREATED INSIDE A FUNCTION .

def second_func():
     x = "JUSTIN BIEBER"
     print ( "MY FULL NAME IS " + x )

second_func()   

print( "THE GLOBAL VARIABLE IS" , x )