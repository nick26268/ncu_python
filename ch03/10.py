#10

n = int( input("> ") )

#上半部

for i in range( n ) :

    for s in range( 2*n-1 ) :

        if s >= n : s = 2*n-2-s

        for t in range( s+1 ) :

            if i < n-1-s :
                
                print( " " , end = " " )
            
            else :

                print( s+1 , end = " " )
    
    print()

#下半部

for i in range( n-1 , -1 , -1 ) :

    for s in range( 2*n-1 ) :

        if s >= n : s = 2*n-2-s

        for t in range( s+1 ) :

            if i < n-1-s :
                
                print( " " , end = " " )
            
            else :

                print( s+1 , end = " " )
    
    print()


