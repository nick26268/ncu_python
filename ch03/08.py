#7

n = int( input("> ") )

for i in range( n ) :

    for s in range( n-1 , 0 , -1 ) :

        for t in range( 2*(s+1) ) :

            if i+1 >= n-s : 
                
                if( t-i == 2*(s+1)-n ) :

                    print( "\\" , end = "" )
                
                elif( i+t == n-1 ) :

                    print( "/" , end = "" )

                elif( t-i < 2*(s+1)-n and i+t > n-1 ) :

                    print( " " , end = "" )
                
                else :

                    print( "|" , end = "" )

            else : 

                print( "|" , end = "" )

    for s in range( n ) :

        if s > n-1 : s = 2*n-1-s-1

        for t in range( 2*(s+1) ) :

            if i+1 >= n-s : 
                
                if( t-i == 2*(s+1)-n ) :

                    print( "\\" , end = "" )
                
                elif( i+t == n-1 ) :

                    print( "/" , end = "" )

                elif( t-i < 2*(s+1)-n and i+t > n-1 ) :

                    print( " " , end = "" )
                
                else :

                    print( "|" , end = "" )

            else : 

                print( "|" , end = "" )

    print()
        
#下半部

for i in range( n-1 , -1 , -1 ) :

    for s in range( n-1 , 0 , -1 ) :

        for t in range( 2*(s+1) ) :

            if i+1 >= n-s : 
                
                if( t-i == 2*(s+1)-n ) :

                    print( "/" , end = "" )
                
                elif( i+t == n-1 ) :

                    print( "\\" , end = "" )

                elif( t-i < 2*(s+1)-n and i+t > n-1 ) :

                    print( " " , end = "" )
                
                else :

                    print( "|" , end = "" )

            else : 

                print( "|" , end = "" )

    for s in range( n ) :

        if s > n-1 : s = 2*n-1-s-1

        for t in range( 2*(s+1) ) :

            if i+1 >= n-s : 
                
                if( t-i == 2*(s+1)-n ) :

                    print( "/" , end = "" )
                
                elif( i+t == n-1 ) :

                    print( "\\" , end = "" )

                elif( t-i < 2*(s+1)-n and i+t > n-1 ) :

                    print( " " , end = "" )
                
                else :

                    print( "|" , end = "" )

            else : 

                print( "|" , end = "" )

    print()
        

