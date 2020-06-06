#5

n = int( input("> ") )

for i in range( n ) :
    
    if ( i == n-1 ) :
        print( "2" , end = " " )
    
    else :
        print( "1" , end = " " )

print()

for k in range( n-2 ) :

    for i in range( n ) :

        if ( i == 0 ) :
            print( "4" , end = " " )
        
        elif ( i == n-1 ) :
            print( "2" , end = " " )
        
        else :
            print( " " , end = " " )
    
    print()

for i in range( n ) :

    if( i == 0 ) :

        print( "4" , end = " " )
    
    else :

        print( "3" , end = " " )

print()