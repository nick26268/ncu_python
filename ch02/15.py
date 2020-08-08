#15

n = int( input("> ") )

hh , vv = chr(9472) ,chr(9474)
nw , ne , sw , se = chr(9484) , chr(9488) , chr(9492) , chr(9496)

index = n/2

if index % 1 != 0 : index = int(index)+1

for i in range( n ) :

    for k in range( 3 ) :

        if k == 0 : 

            for j in range( n ) :

                if j-i == 0 and i < index :

                    print( nw , end = "" )
                
                elif j-i == 0 and i >= index :

                    print( se , end = "" )
                
                elif i+j == n-1 and i >= index :

                    print( sw , end = "" )
                
                elif i+j == n and i < index :

                    print( ne , end = "" )

                elif j-i < 0 and i+j < n  or i+j > n and j-i > 0 :

                    print( vv , end = "" )

                else :

                    print( hh , end = "" )
        
        elif k == 1 :

            if i == 0 : print( ne , end = "" )

            elif i == n-1 : print( sw , end = "" )

            else : print( vv , end = "" )
        
        else :

            for j in range( n ) :

                if j-i == 0 and i < n-index :

                    print( nw , end = "" )
                
                elif j-i == 0 and i >= n-index :

                    print( se , end = "" )
                
                elif i+j == n-2 and i >= n-index :

                    print( sw , end = "" )
                
                elif i+j == n-1 and i < n-index :

                    print( ne , end = "" )

                elif j-i < 0 and i+j < n-2  or i+j > n-2 and j-i > 0 :

                    print( vv , end = "" )

                else :

                    print( hh , end = "" )

            
                
    print()