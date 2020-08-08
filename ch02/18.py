#18

n = int( input("> ") )

index = n / 2 

if index % 1 != 0 : index = int(index)+1

for i in range( 2*n-3 ) :

    for k in range( int(index) ) :

        for j in range( 2*n+1 ) :

            if j-i <= 0 and i < n :

                print( 2*k+1 , end = "" )
            
            elif j-i > 3 and i > n-4 :

                if n % 2 != 0 and k == index-1 :

                    print( " " + (" " if j==2*n else "") , end = "" )

                else :

                    print( str(2*k+2) + (" " if j == 2*n else "") , end = "" )
                
            else :

                print( " " + (" " if j == 2*n else "") , end = "" )
    
    print()

        

