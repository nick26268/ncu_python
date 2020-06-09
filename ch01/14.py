#14

n = int( input("> ") )

for i in range( n ) :

    num = 1

    for j in range( n ) :

        print( str(num%10) * i , end = "\\" )

        print( 2 * " " * (n-i-1) , end = "/" )

        num += 1

        print( str(num%10) * i , end = "" )
    
    print()

for i in range( n-1 , -1 , -1 ) :

    num = 1

    for j in range( n ) :

        print( str(num%10) * i , end = "/" )

        print( 2 * " " * (n-i-1) , end = "\\" )

        num += 1

        print( str(num%10) * i , end = "" )
    
    print()

print()