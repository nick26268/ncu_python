#19

hh , vv = chr(9472) , chr(9474)
nw , ne , sw , se = chr(9484) , chr(9488) , chr(9492) , chr(9496)

n = int( input("> ") )

for i in range( 2*n+1 ) :

    for k in range( n ) :

        for j in range( 2*n+1 ) :

            if i+j == n-1 :

                print( nw , end = "" )
            
            elif j-i == n+1 :

                print( ne , end = "" )
            
            elif i+j == n and i > 0 and i < n :

                print( se , end = "" )

            elif j-i == n and i > 0 and i < n :

                print( sw , end = "" )

            elif i == n and (j == 0 or j == 2*n) :

                print( vv , end = "" )
            
            elif j-i == -n-1 :
                
                print( sw , end = "" )

            elif j-i == -n and i < 2*n :

                print( ne , end = "" )
            
            elif i+j == 3*n+1 :

                print( se , end = "" )

            elif i+j == 3*n and i < 2*n :

                print( nw , end = "" )

            elif i == 0 and j == n or i == 2*n and j == n :

                print( hh , end = "" ) 

            else :

                print( " " , end = "" )
    
    print()

        