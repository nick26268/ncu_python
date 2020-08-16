#15

n = int( input("> ") )

for i in range( 5 ) :

    for s in range( 5 ) :

        for j in range( n ) :

            for t in range( n ) :

                if i == 0 or i == 2 or i == 4 or i == 1 and j == n-1 or i == 3 and j == 0 :

                    if s == 0 or s == 2 or s == 4 or s == 1 and t == n-1 or s == 3 and t == 0 :

                        print( "2" + (" " if t == n-1 else "") , end = "" )
                    
                    else :

                        print( " " + (" " if t == n-1 else "") , end = "" )
                
                else :

                    print( " " + (" " if t == n-1 else "") , end = "" )
        
        print()
    

