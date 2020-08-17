#16

n = int( input("> ") )

for i in range( 7 ) :

    for s in range( n ) :

        for j in range( 5 ) :

            if i == 2 or i == 4 or j == 2 or (j == 0 or j == 4) and 1 < i < 5 :

                print( "中"*n , end = "" )
            
            else :

                print( "  "*n , end = "" )
        
        print()


        