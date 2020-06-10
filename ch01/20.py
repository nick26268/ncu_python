#20

n = int( input("> ") )

num = 1

for i in range( n ) :

    num += i

    for k in range( i+1 ) :

        print( str((num+k)%10) * (2*n-1) , end = " " )
    
    print()

    for j in range( n-2 ) :

        for k in range( i+1 ) :

            print( str((num+k)%10) , " " * (2*n-3) , str((num+k)%10) , sep = "" , end = " " )
        
        print()
    
    for k in range( i+1 ) : 

        print( str((num+k)%10) * (2*n-1) , end = " " )

    print( "\n" )