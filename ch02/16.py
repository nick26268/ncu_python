#16 

n = int( input("> ") )

hh , vv = chr(9472) ,chr(9474)
nw , ne , sw , se = chr(9484) , chr(9488) , chr(9492) , chr(9496)

for i in range( 2*n-1 ) :

    for k in range( n ) :

        for j in range( n ) :

            if j == 0 and i == k :

                print( nw , end = "" )

            elif j == 0 and i == n+k-1 :

                print( sw , end = "" )

            elif j == n-1 and i == k :

                print( ne , end = "" )

            elif j == n-1 and i == n+k-1 :

                print( se , end = "" )
            
            elif j > 0 and j < n-1 and i >= k and i <= n+k-1 :

                print( hh , end = "" )
            
            elif (j == 0 or j == n-1) and i >= k and i <= n+k-1 : 

                print( vv , end = "" )
                
            else :

                print( " " , end = "" )

    print() 