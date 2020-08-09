#1

n = int( input("> ") )

for i in range( n ) :

    for s in range( n ) :

        print( n*(n-i-1)*" " , end = "" )

        for j in range( n ) :

            for t in range( 2*n-1 ) :

                if j-i <= 0 :

                    if t-s == n-1 or t+s == n-1 or s == n-1 :

                        print( str(j+1) + (" " if t == 2*n-2 else "") , end = "" )
                    
                    else :

                        print( " " + (" " if t == 2*n-2 else "") , end = "" )
                
                else :

                    print( " " , end = "" )
        
        print()