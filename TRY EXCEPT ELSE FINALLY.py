# try BLOCK USED TO TEST A UNIT OF CODE FOR ERROR .

# except BLOCK USED TO HANDLE THE ERROR .

# else BLOCK IS USED TO EXECUTE THE CODE WHEN THERE IS NO ERROR .

# finally IS USED TO EXECUTE THE CODE REGARDLESS OF try AND except RESULT .

# try BLOCK AND except BLOCK .

# EXAMPLE ONE

a = 64
try:
   print(a)
except:
   print ( "NAME a IS NOT DEFINED" )   

# EXAMPLE TWO

try:
   print(b)
except:
   print ( "NAME b IS NOT DEFINED" ) 

# EXAMPLE THREE

c = 48
try:
   print(c)
except:
   pass  

# EXAMPLE FOUR

try:
   print(d)
except:
   print ( "AN ERROR OCCURED FOR d VARIABLE" )  

# MANY except BLOCKS CAN ASLO BE DEFINED .

try:
   print(e)
except NameError:
   print ( "NAME e IS NOT DEFINED" )     
except:
   print ( "AN ERROR OCCURED FOR e VARIABLE" )  

# try BLOCK , except BLOCK AND else BLOCK .  

# EXAMPLE ONE

try:
   print ( "GOOD MORNING" )
except:
   print ( "SOMETHING WENT WRONG WITH GOOD MORNING" )
else:
   print ( "NOTHING WENT WRONG WITH GOOD MORNING" ) 

# EXAMPLE TWO

try:
   print(f)
except:
   print ( "NAME f IS NOT DEFINED" )
else:
   print ( "NO ERROR OCCURED FOR f VARIABLE" ) 

# try BLOCK , except BLOCK AND finally BLOCK .   

# EXAMPLE ONE

try:
   print(g)
except:
   print ( "NAME g IS NOT DEFINED" ) 
finally:
   print ( "NO ERROR OCCURED FOR g VARIABLE" )   

# EXAMPLE TWO

try:
   print ( "GOOD NIGHT" )
except:
   print ( "SOMETHING WENT WRONG WITH GOOD NIGHT" )
finally:
   print ( "NOTHING WENT WRONG WITH GOOD NIGHT" ) 

# EXAMPLE THREE 

try:
    h = open ( "FILEFOUR.txt" )
    try:
        h.write ( "MY FULL NAME IS TOM CRUISE" )
    except:
        print ( "SOMETHING WENT WRONG WHILE WRITING TO THE FILE" ) 
    finally:
        h.close()
except:
   print ( "SOMETHING WENT WRONG WHILE OPENING THE FILE" )        