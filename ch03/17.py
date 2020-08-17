#17

n = int( input("> ") )

for i in range( n+1 ) :

    for s in range( 2 ) :

        for x in range( 2 ) :

            if x == 0 : n_th = 0 
            else : n_th = -1

            for j in range( n ) : 

                for t in range( 3 ) :

                    if i > n-2-j and i < n+1-j :

                        print( str(j+1) + (" " if t == 2 else "") , end = "" )
                    
                    else :

                        print( " " + (" " if t == 2 else "") , end = "" )
            
            for j in range( n-2 , n_th , -1 ) : 

                for t in range( 3 ) :

                    if i > n-2-j and i < n+1-j :

                        print( str(j+1) + (" " if t == 2 else "") , end = "" )
                    
                    else :

                        print( " " + (" " if t == 2 else "") , end = "" )
            
        print()

        