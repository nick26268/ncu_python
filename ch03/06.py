#6

#上半部

n = int( input("> ") )

for i in range( n-1 ) :

    for s in range( 3 ) :

        print( (n-i-1)*3*" " , end = "" )

        for j in range( 2*n-1 ) :

            if j > n-1 : j = abs(2*n-2-j)

            for t in range( j+1 ) :

                if t-i <= -n+1+j : 

                    print( str(j+2-(n-i))*5 , end = " " )
                
                else :

                    print( " "*5 , end = " " )
        
        print()

#下半部

for i in range( n-1 , -1 , -1 ) :

    for s in range( 3 ) :

        print( (n-i-1)*3*" " , end = "" )

        for j in range( 2*n-1 ) :

            if j > n-1 : j = abs(2*n-2-j)

            for t in range( j+1 ) :

                if t-i <= -n+1+j : 

                    print( str(j+2-(n-i))*5 , end = " " )
                
                else :

                    print( " "*5 , end = " " )
        
        print()