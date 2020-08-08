#12

n = int( input("> ") )

for i in range( 2*n ) :

    for j in range( 3 ) :

        if j != 1 :
            
            for k in range( 2*n ) :

                if i > n-1 :

                    if k-i == 0 :

                        print( "\\" , end = "" )
                    
                    elif i+k == 2*n-1 :

                        print( "/" , end = "" )

                    elif i == 2*n-1 :

                        print( "_" , end = "" )

                    else :

                        print( " " , end = "" )

                else :

                    print( " " , end = "" )
        
        else :

            for k in range( 4*n ) :

                if k-i == 2*n :

                    print( "\\" , end = "" )

                elif i+k == 2*n-1 :

                    print( "/" , end = "" )

                elif i == 2*n-1 :

                    print( "_" , end = "" )

                else :

                    print( " " , end = "" ) 
    
    print()