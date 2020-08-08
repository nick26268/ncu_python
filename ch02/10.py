#10

n = int( input("> ") )

for i in range( -n+1 , n ) :

    for j in range( -n+1 , n ) :

        max_num = max(abs(i),abs(j))
        index_i = n-abs(i)-1
        index_j = n-abs(j)-1

        if index_i + index_j < n-1 :

            print( " " , end = " " )     

        else :

            print( n-max_num , end = " " )
    
    print()