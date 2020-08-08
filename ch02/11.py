#11

n = int( input("> ") )

for i in range( 2*n-1 ) :

    for num in range( n+1 ) :

        for j in range( 2*n-1 ) :

            if num == n and j > 0 :
                
                break 

            if ( i+j == n-1 or i+j == 3*n-2 ) and i != n-1 :

                print("/" , end = "" )
            
            elif ( j-i == n or i-j == n-1 ) and i!= n-1 :

                print( "\\" , end = "" )
            
            elif ( i == n-1 and ( j == 0 or j == 2*n-1 ) ) :
                
                print( "x" , end = "" )
            
            elif ( i+j > n-1 and i+j < 3*n-2 and i-j < n-1 and j-i < n ) :

                print( "|" , end = "" ) 
            
            else :

                print(" " , end = "" )
        
    print()

