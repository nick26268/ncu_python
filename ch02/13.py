#13

n = int( input("> ") )

the_third_mountain_width = 1.5 * n 

if the_third_mountain_width % 1 != 0 : the_third_mountain_width = int(the_third_mountain_width) + 1 

for i in range( 2*n ) :

    for j in range( 3 ) :

        if j == 0 :
            
            for k in range( 2*n ) :

                if i > n-1 :

                    if k-i == 0 :

                        print( "\\" , end = "" )
                    
                    elif i+k == 2*n-1 :

                        print( "/" , end = "" )

                    elif k-i < 0 and i+k > 2*n-1 :

                        print( "_" , end = "" )

                    else :

                        print( " " , end = "" )

                else :

                    print( " " , end = "" )
        
        elif j == 1 :

            for k in range( 4*n ) :

                if k-i == 2*n :

                    print( "\\" , end = "" )

                elif i+k == 2*n-1 :

                    print( "/" , end = "" )

                elif k-i < 2*n and i+k > 2*n-1 :

                    print( "_" , end = "" )

                else :

                    print( " " , end = "" ) 
        
        else :

            for k in range( 2 * int(the_third_mountain_width) ) :

                if i < 2*n-int(the_third_mountain_width) :

                    print( " " , end = "" ) 
                
                else :

                    if k-i == 2*(int(the_third_mountain_width)-n) :

                        print( "\\" , end = "" )

                    elif i+k == 2*n-1 :

                        print( "/" , end = "" )

                    elif k-i < 2*(int(the_third_mountain_width)-n) and i+k > 2*n-1 :

                        print( "_" , end = "" )

                    else :

                        print( " " , end = "" )                            

    print()