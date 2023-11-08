# GET THE dir OF datetime MODULE .

import datetime
print ( dir(datetime) )

# GET THE CURRENT DATE AND CURRENT TIME .

import datetime
a = datetime.datetime.today()
print(a)

import datetime
b = datetime.datetime.now()
print(b)

# RETURN THE YEAR FROM THE CURRENT DATE AND CURRENT TIME .

import datetime
b = datetime.datetime.now()
print ( "THE CURRENT YEAR IS" , b.year )

# RETURN THE MONTH FROM THE CURRENT DATE AND CURRENT TIME .

import datetime
b = datetime.datetime.now()
print ("THE CURRENT MONTH IS" , b.month )

# RETURN THE DAY OF MONTH FROM THE CURRENT DATE AND CURRENT TIME .

import datetime
b = datetime.datetime.now()
print ( "THE CURRENT DAY OF MONTH IS" , b.day )

# RETURN THE HOUR FROM THE CURRENT DATE AND CURRENT TIME .

import datetime
b = datetime.datetime.now()
print ( "THE CURRENT HOUR IS" , b.hour )

# RETURN THE MINUTE FROM THE CURRENT DATE AND CURRENT TIME .

import datetime
b = datetime.datetime.now()
print ( "THE CURRENT MINUTE IS" , b.minute )

# RETURN THE SECOND FROM THE CURRENT DATE AND CURRENT TIME .

import datetime
b = datetime.datetime.now()
print ( "THE CURRENT SECOND IS" , b.second )

# RETURN THE MICRO-SECOND FROM THE CURRENT DATE AND CURRENT TIME .

import datetime
b = datetime.datetime.now()
print ( "THE CURRENT MICRO-SECOND IS" , b.microsecond )

# datetime FUNCTION IS USED TO CREATE DATE OBJECTS .

# EXAMPLE ONE 

import datetime
c = datetime.datetime (2016,8,24)
print(c)

# EXAMPLE TWO

import datetime
d = datetime.datetime (2012,4,14,16,22,48)
print(d)

# EXAMPLE THREE

import datetime
e = datetime.datetime (2018,10,18,20,52,4,128256)
print(e) 

# EXAMPLE FOUR

import datetime
f = datetime.datetime (2008,12,30,6,28,36,512)
print(f) 

# THE strftime FUNCTION .

# EXAMPLE ONE 

import datetime
f = datetime.datetime (2008,12,30,6,28,36,512)
print ( f.strftime("%A") )

# EXAMPLE TWO

import datetime
f = datetime.datetime (2008,12,30,6,28,36,512)
print ( f.strftime("%B") )

# EXAMPLE THREE

import datetime
f = datetime.datetime (2008,12,30,6,28,36,512)
print ( f.strftime("%C") )

# EXAMPLE FOUR

import datetime
f = datetime.datetime (2008,12,30,6,28,36,512)
print ( f.strftime("%D") )