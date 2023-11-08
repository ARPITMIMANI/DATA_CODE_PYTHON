# EXAMPLE ONE

try:
    raise Exception ( "MEMORY ERROR" )
except Exception as e:
    print(e)

# EXAMPLE TWO    

try:
    raise Exception ( "MemoryError" )
except Exception as e:
    print(e)

# EXAMPLE THREE

try:
    raise MemoryError ( "MEMORY ERROR" )
except MemoryError as m:
    print(m)

# EXAMPLE FOUR
    
try:
    raise MemoryError ( "MemoryError" )
except MemoryError as m:
    print(m)

# EXAMPLE FIVE

try:
    raise Exception ( "MODULE NOT FOUND ERROR" )
except Exception as m:
    print(m)  

# EXAMPLE SIX

try:
    raise ModuleNotFoundError ( "ModuleNotFoudError" )
except ModuleNotFoundError as m:
    print(m)  

# EXAMPLE SEVEN

class accident ( Exception ) :

    def __init__ ( self , message ) :
        self.message =  message    

    def print_message ( self ) :
        print ( "THE MESSAGE IS :" , self.message )   

try:
    raise accident ( "TWO TRUCKS COLLIDED" )
except accident as a:
    a.print_message()           
   
# EXAMPLE EIGHT

class detour ( Exception) :

    def __init__ ( self , msg ) :
        self.msg = msg

    def handle_situation ( self ) :
        print ( "HANDLE SITUATION :" , self.msg )

try:
    raise detour ( "ACCIDENT OCCURED TAKE DETOUR" )
except detour as d: 
    d.handle_situation()           