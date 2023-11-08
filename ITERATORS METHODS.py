# ITERATOR : IT IS AN OBJECT WHICH IMPLEMMENTS THE ITERATORS PROTOCOL .

# ITERATOR HAS 2 METHODS : __init__() AND __next__() 

# ALL OF THE 4 DATA TYPES THAT IS LIST , TUPLES , SET AND DICTIONARY ARE ITERATORS .

# LIST AS ITERATORS .

a1 = [ "IRELAND" ,  "FINLAND" , "NORWAY" , "SWEDEN" , "DENMARK" , "WALES" , "ICELAND" , "SCOTLAND" , "ENGLAND" , "GREENLAND" ] 
a2 = iter(a1)

print ( next (a2) )
print ( next (a2) )
print ( next (a2) )
print ( next (a2) )
print ( next (a2) )
print ( next (a2) )
print ( next (a2) )
print ( next (a2) )
print ( next (a2) )
print ( next (a2) )

print ( "FIRST ITERATION IS FINISHED" )

# TUPLE AS ITERATORS .

b1 = ( "PURPLE" , "YELLOW" , "GREEN" , "ORANGE" , "BROWN" , "RED" , "SILVER" , "VIOLET" , "GREY" , "BLUE" )
b2 = iter(b1)

print ( next (b2) )
print ( next (b2) )
print ( next (b2) )
print ( next (b2) )
print ( next (b2) )
print ( next (b2) )
print ( next (b2) )
print ( next (b2) )
print ( next (b2) )
print ( next (b2) )

print ( "SECOND ITERATION IS FINISHED" )

# SET AS ITERATORS .

c1 = { "ONE" , "TWO" , "THREE" , 'FOUR' , "FIVE" , "SIX" , "SEVEN" , "EIGHT" , "NINE" , "TEN" }
c2 = iter(c1)

print ( next (c2) )
print ( next (c2) )
print ( next (c2) )
print ( next (c2) )
print ( next (c2) )
print ( next (c2) )
print ( next (c2) )
print ( next (c2) )
print ( next (c2) )
print ( next (c2) )

print ( "THIRD ITERATION IS FINISHED" )

# DICTIONARY AS ITERATORS .

d1 = { "JIM":82 , "TOM":74 , "DAN":88 , "FIN":92 , "LEO":78 , "REX":84 }
d2 = iter(d1)

print ( next (d2) )
print ( next (d2) )
print ( next (d2) )
print ( next (d2) )
print ( next (d2) )
print ( next (d2) )

print ( "FOURTH ITERATION IS FINISHED" )

# STRING AS ITERATORS .

e1 = "WATERMELON"
e2 = iter(e1)

print ( next (e2) )
print ( next (e2) )
print ( next (e2) )
print ( next (e2) )
print ( next (e2) )
print ( next (e2) )
print ( next (e2) )
print ( next (e2) )
print ( next (e2) )
print ( next (e2) )

print ( "FIFTH ITERATION IS FINISHED" )

# LOOPING ITERATOR USING for LOOP .

f = "PYTHON LANGUAGE"
for item in f:
    print(item)

print ( "SIXTH ITERATION IS FINISHED" )   

# TO CREATE A ITERATOR USING OBJECT OR CLASS WE NEED TO IMPLEMENT __iter__() AND __next__() TO THE OBJECT .

# ALL CLASSES HAVE AN __init__() FUNCTION WHICH IS USED TO DO THE INITIALIZATION .

# PRINT ALL NATURAL NUMBERS FROM 1 TO 6 ONLY .

# CASE ONE

class number:

    def __iter__ ( self ) :
        self.num = 1
        return self
    
    def __next__ ( self ) :
        i = self.num
        self.num = self.num + 1
        return i

num1 = number()
num2 = iter(num1)

print ( next (num2) )
print ( next (num2) )
print ( next (num2) )
print ( next (num2) )
print ( next (num2) )
print ( next (num2) )

print ( "CASE ONE COMPLETED" )

# CASE TWO

class integers:

    def __iter__ ( abcd ) :
        abcd.ints = 1
        return abcd
    
    def __next__ ( abcd ) :
        j = abcd.ints
        abcd.ints = abcd.ints + 1
        return j
    
int1 = integers()
int2 = iter(int1) 

print ( next (int2) )
print ( next (int2) )
print ( next (int2) )
print ( next (int2) )
print ( next (int2) )
print ( next (int2) )

print ( "CASE TWO COMPLETED" )

# CASE THREE

class integers:

    def __iter__ ( abcd ) :
        abcd.ints = 1
        return abcd
    
    def __next__ ( abcdef ) :
        j = abcdef.ints
        abcdef.ints = abcdef.ints + 1
        return j
    
int1 = integers()
int2 = iter(int1) 

print ( next (int2) )
print ( next (int2) )
print ( next (int2) )
print ( next (int2) )
print ( next (int2) )
print ( next (int2) )

print ( "CASE THREE COMPLETED" )

# StopIteration STATEMENT IS USED TO PREVENT THE ITERATION TO GO OVER FOREVER .

# PRINT ALL THE NATURAL NUMBERS FROM 1 TO 20 ONLY .

class value:

    def __iter__ ( self ) :
        self.fig = 1
        return self
    
    def __next__ ( self) :

        if self.fig <= 20 :
            i= self.fig
            self.fig = self.fig + 1
            return i
        
        else:
            raise StopIteration
        
val1 = value()
val2 = iter(val1)

for j in val2:
    print(j)

print ( "ITERATION COMPLETED" )    
