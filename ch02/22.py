#22

n = int( input("請輸入奇數> ") )

for i in range( 3 ) :

    for s in range( n ) :

        for j in range( 3 ) :

            for t in range( n ) :

                if j-i == 0 or i+j == 2 :

                    if t-s == 0 and s+t == n-1 :

                        print( "x" , end = "" )
                    
                    elif t-s == 0 :

                        print( "\\" , end = "" )
                    
                    elif s+t == n-1 :

                        print( "/" , end = "" )
                    
                    else :

                        print( " " , end = "" )
                
                else :

                    print( " " , end = "" )
        
        print()