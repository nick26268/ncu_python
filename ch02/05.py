#5

for i in range( 9 ) :
    
    for j in range( 9 ) :

        print( "{:>3}".format(i+1) , end = " " )
    
    print()

    for j in range( 9 ) :

        print( "x{:>2}".format(j+1) , end = " " )
    
    print()

    for j in range( 9 ) :

        print( "---" , end = " " )

    print()

    for j in range( 9 ) :
        
        print( "{:>3}".format((i+1)*(j+1)) , end = " " )
    
    print("\n")
