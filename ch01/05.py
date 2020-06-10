#5

n = int( input("> ") )

for i in range( n-1 ) :

    print( "1" , end = " " )

print( "2" )

for i in range( n-2 ) :

    print( "4" , end = " " )

    for j in range( n-2 ) :

        print( " " , end = " " )
    
    print( "2" )

print( "4" , end = " " )

for i in range( n-1 ) :
    print( "3" , end = " " )

print()