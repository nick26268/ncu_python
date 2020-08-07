#6

n = int( input("> ") )

for i in range( n ) :

    for j in range( 4*n-3 ) :
        
        if( j-i == 0 or i+j == 2*n-2 or j-i == 2*n-2 or i+j == 4*n-4 ) :
            print( "*" , end = "" )
        
        else :
            print( " " , end = "" )
    
    print()