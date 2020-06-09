#13

n = int( input("> ") )

for i in range( n ) :

    for j in range( n ) :

        print( " " * i , end = "\\" )

        print( 2 * " " * (n-i-1) , end = "/" )

        print( " " * i , end = "" )
    
    print()

for i in range( n-1 , -1 , -1 ) :

    for j in range( n ) :

        print( " " * i , end = "/" )

        print( 2 * " " * (n-i-1) , end = "\\" )

        print( " " * i , end = "" )
    
    print()

print()

