#23

n = int( input("> ") )

for i in range( n ) :

    for k in range( n ) :

        print( " " * ( n-i-1 ) , end = "" )

        for j in range( 2*i+1 ) :

            print( i+1 , end = "" )

        print( " " * ( n-i-1 ) , end = " " )

    print()

print()  