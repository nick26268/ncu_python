#3

n = int( input("> ") )

#上半部

for i in range( n ) :

    if i == n-1 : 

        for s in range( n-1 ) :

            print( (n-i-1)*n*" " , end = "" )

            for j in range( 2*n-1 ) :

                for t in range( 2*n-1 ) :

                    if j-i <= 0 or (j >= n-1 and j-i <= n-1) :

                        if t-s == n-1 or s+t == n-1 or s == n-1 :

                                print( str(s+1) + (" " if t == 2*n-2 else "") , end = "" )
                        
                        else : 
                            
                            print( " " + (" " if t == 2*n-2 else "") , end = "" )
                    
                    else :

                        print( " " + (" " if t == 2*n-2 else "") , end = "" )
                
            print()

    else :

        for s in range( n ) :

            print( (n-i-1)*n*" " , end = "" )

            for j in range( 2*n-1 ) :

                for t in range( 2*n-1 ) :

                    if j-i <= 0 or (j >= n-1 and j-i <= n-1) :

                        if t-s == n-1 or s+t == n-1 or s == n-1 :

                                print( str(s+1) + (" " if t == 2*n-2 else "") , end = "" )
                        
                        else : 
                            
                            print( " " + (" " if t == 2*n-2 else "") , end = "" )
                    
                    else :

                        print( " " + (" " if t == 2*n-2 else "") , end = "" )
                
            print()

#下半部

for i in range( n-1 , -1 , -1 ) :

    for s in range( n-1 , -1 , -1 ) :

        print( (n-i-1)*n*" " , end = "" )

        for j in range( 2*n-1 ) :

            for t in range( 2*n-1 ) :

                if j-i <= 0 or (j >= n-1 and j-i <= n-1) :

                    if t-s == n-1 or s+t == n-1 or s == n-1 :

                        print( str(s+1) + (" " if t == 2*n-2 else "") , end = "" )
                    
                    else : 
                        
                        print( " " + (" " if t == 2*n-2 else "") , end = "" )
                
                else :

                    print( " " + (" " if t == 2*n-2 else "") , end = "" )
            
        print()