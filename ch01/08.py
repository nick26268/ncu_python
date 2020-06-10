#8

n = int( input("> ") )

for i in range( n ) :

    for j in range( i+1 ) :

        print( i+1 , end = " " )
    
    print( 4 * " " * (n-i-1) , end = "" )

    for j in range( i+1 ) :
        
        print( i+1 , end = " " )
    
    print()

print()