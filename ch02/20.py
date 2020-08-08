#20

n = int( input("> ") )

for i in range( 3 ) :

    for s in range( n ) :

        for j in range( 3 ) :

            for t in range( n ) :

                if j-i == 0 or i+j == 2 :

                    if i == 0 and j == 0 :
                        
                        print( "1" , end = "" )
                    
                    elif i == 0 and j == 2 :

                        print( "2" , end = "" )
                    
                    elif i == 1 and j == 1 :

                        print( "3" , end = "" )
                    
                    elif i == 2 and j == 0 :

                        print( "4" , end = "" )
                    
                    elif i == 2 and j == 2 :

                        print( "5" , end = "" )

                else :

                    print( " " , end = "" )
        
        print()