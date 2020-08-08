#17

n = int( input("> ") )

for i in range( 2*n-1 ) :

    for k in range( n ) :

        for j in range( n ) :

            if (j == 0 or j == n-1) and i > k-1 and i < n+k or i == n+k-1 :

                print( str(k+1) + (" " if j == n-1 else "") , end = "" )
            
            else :

                print( " " + (" " if j == n-1 else "")  , end = "" )

    print() 