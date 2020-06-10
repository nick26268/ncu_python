#28

n = int( input("> ") )

for i in range( n ) :

    print( " " * (n-1) * n , end = "" )

    for j in range( n ) :

        print( n , end = "" )
    
    print() 

for i in range( n-2 , -1 , -1 ) :

    for j in range( n ) :

        print( " " * n * i , end = "" )

        for s in range( n ) :

            print( i+1 , end = "" )

        print( " " * n * (2*n-1-2*(i+1)) , end = "" )

        for s in range( n ) :

            print( i+1 , end = "" )

        print() 

print()


