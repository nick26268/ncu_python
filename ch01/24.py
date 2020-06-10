#24

n = int( input("> ") )

for k in range( n ) :

    print( " " * (n-1) , "1" , " " * (n-1) , sep = "" , end = " " )

print()



for i in range( n-2 ) :

    for k in range( n ) :

        print( " " * (n-2-i) , i+2 , " " * (1+2*i) , i+2 , " " * (n-2-i) , sep = "" , end = " " )
    
    print()

for k in range( n ) :

    print( str(n) * (2*n-1) , end = " " )

print()
