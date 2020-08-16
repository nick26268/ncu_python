#14

n = int( input("> ") )

for i in range( n ) :

    for s in range( 2 ) :

        for j in range( 2*n-3 ) :

            for t in range( 2 ) :

                if j == 0 or j == 2*n-4 or (j-i == 0 or j+i == 2*n-4) and i < n-1 :

                    print( "M" , end = "" )
                
                elif j-i == -1 and s == 0 and t == 1 and i < n-1 :

                    print( "M" , end = "" )
                
                elif j-i == 1 and s == 1 and t == 0 and i < n-2 :

                    print( "M" , end = "" )

                elif j+i == 2*n-5 and s == 1 and t == 1 and i < n-2 :

                    print( "M" , end = "" )

                elif j+i == 2*n-3 and s == 0 and t == 0 and i < n-1 :

                    print( "M" , end = "" )

                else :

                    print( " " , end = "" )
        
        print()