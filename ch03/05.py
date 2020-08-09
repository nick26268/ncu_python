#5

n = int( input("> ") )

for i in range( n ) :

    for s in range( 3 ) :

        print( (n-i-1)*3*" " , end = "" )

        for j in range( n ) :

            for t in range( j+1 ) :

                if t-i <= -n+1+j : 

                    print( str(j+2-(n-i))*5 , end = " " )
                
                else :

                    print( " "*5 , end = " " )
        
        print()