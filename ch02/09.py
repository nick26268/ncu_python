#9

n = int( input("> ") )

for i in range( -n+1 , n ) :

    for j in range( -n+1 , n ) :

        max_num = max(abs(i),abs(j))
        print( n-max_num , end = " " )
    
    print()