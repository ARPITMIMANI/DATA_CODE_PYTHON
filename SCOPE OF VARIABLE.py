# SCOPE : A VARIABLE IS ONLY AVAILABLE FROM INSIDE THE REGION IT IS CREATED .

# FIRST EXAMPLE OF LOCAL SCOPE .

def localscope():
    a = 400
    print(a)

localscope()   

# SECOND EXAMPLE OF LOCAL SCOPE .

# CREATE A FUNCTION INSIDE A FUNCTION .

def outerfunc():
    b = 324
    def innerfunc():
        print(b)
    innerfunc()

outerfunc()  

# EXAMPLE OF GLOBAL SCOPE .

c = 676

def globalscope():
    print(c)

globalscope()

# IF THE NAME OF VARIABLE IS SAME BUT WITH DIFFERENT VALUES THEN PRIORITY IS GIVEN TO THE LOCAL VARIABLE FIRST .

# PYTHON WILL TREAT THE LOCAL VARIABLE AND GLOBAL VARIABLE AS SEPARATE VARIABLES .

d = 256

def myvar():
    d = 144
    print(d)

myvar()
print(d)    

# global KEYWORD IS USED TO CREATE A GLOBAL VARIABLE LOCALLY .

# CASE ONE 

def variable():
    global e 
    e = 576
    print(e)

variable()
print ( e , "IS FIRST CASE RESULT" )   

# CASE TWO

def variable():
    global e 
    e = 576

variable()
print ( e , "IS SECOND CASE RESULT" ) 

# global KEYWORD IS USED TO MAKE A CHANGE TO GLOBAL VARIABLE INSIDE THE FUNCTION .

# CASE ONE 

f = 484
def change():
    global f 
    f = 196
    print(f)

change()
print ( f , "IS FIRST CASE RESULT" ) 

# CASE TWO

f = 484
def change():
    global f 
    f = 196

change()
print ( f , "IS SECOND CASE RESULT" )