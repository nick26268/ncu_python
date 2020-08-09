#4

n = int( input("> ") )

for i in range( n ) :

    if i == n-1 : 

        for s in range( n-1 ) :

            print( (n-i-1)*n*" " , end = "" )

            for j in range( n ) :

                for t in range( 2*n-1 ) :

                    if j-i <= 0 :

                        if t-s == n-1 or t+s == n-1 or s == n-1 :

                            if j-i == 0 or j == 0 :

                                print( str(s+1) + (" "if t == 2*n-2 else "") , end = "" )

                            else :

                                print( " " + (" " if t == 2*n-2 else "") , end = "" )
                        
                        else :

                            print( " " + (" " if t == 2*n-2 else "") , end = "" )
                    
                    else :

                        print( " " , end = "" )
            
            print()
    
    else :

        for s in range( n ) :

            print( (n-i-1)*n*" " , end = "" )

            for j in range( n ) :

                for t in range( 2*n-1 ) :

                    if j-i <= 0 :

                        if t-s == n-1 or t+s == n-1 or s == n-1 :

                            if j-i == 0 or j == 0 :

                                print( str(s+1) + (" " if t == 2*n-2 else "") , end = "" )
                            
                            else :

                                print( " " + (" " if t == 2*n-2 else "") , end = "" ) 
                        
                        else :

                            print( " " + (" " if t == 2*n-2 else "") , end = "" )
                    
                    else :

                        print( " " , end = "" )
        
            print()

#下半部

for i in range( n-1 , -1 , -1 ) :

    for s in range( n-1 , -1 , -1 ) :

        print( (n-i-1)*n*" " , end = "" )

        for j in range( n ) :

            for t in range( 2*n-1 ) :

                if j-i <= 0 :

                    if t-s == n-1 or t+s == n-1 or s == n-1 :

                        if j-i == 0 or j == 0 :

                            print( str(s+1) + (" " if t == 2*n-2 else "") , end = "" )
                        
                        else :

                            print( " " + (" " if t == 2*n-2 else "") , end = "" )
                    
                    else :

                        print( " " + (" " if t == 2*n-2 else "") , end = "" )
                
                else :

                    print( " " , end = "" )
        
        print()