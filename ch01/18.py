#18

n = int( input("> ") )

for i in range( n ) :

    for j in range( i ) :

        print( " " * n , end = " " )
    
    for j in range( n-i ) :

        print( str(i+j+1) * n , end = " " )
    
    print()

print()