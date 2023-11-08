# SYNTAX OF LAMBDA FUNCTION 
# lambda argumnets : expression 

# EXAMPLE OF LAMBDA FUNCTION WITH ONE ARGUMENT .

lam1 = lambda a : a * 4

print ( lam1 (16) )
print ( lam1 (24) )
print ( lam1 (12) )
print ( lam1 (20) )

# EXAMPLE OF LAMBDA FUNCTION WITH TWO ARGUMENT .

lam2 = lambda b , c : b + c 

print ( lam2 (40,48) )
print ( lam2 (30,36) )

# EXAMPLE OF LAMBDA FUNCTION WITH THREE ARGUMENT .

lam3 = lambda d , e , f  : d + e + f  

print ( lam3 (60,80,100) )
print ( lam3 (70,90,120) )

# CREATE AND CALL A FUNCTION USING lambda FUNCTION .

def product_func ( g ) :
    return lambda h : g * h * 8

two_times = product_func(2)
print ( two_times (100) )

three_times = product_func(3) 
print ( three_times (100) )

four_times = product_func(4)
print ( four_times (100) )

five_times = product_func(5)
print ( five_times (100) )

six_times = product_func(6)
print ( six_times (100) )