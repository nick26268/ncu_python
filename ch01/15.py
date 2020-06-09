#15

n = int( input("> ") )

for i in range( n ) :

    start_num = 0
    
    for j in range( n ) :

        start_num += 1
        print( str(start_num%10) * (n-i) , end = "/" )
        start_num += 1
        print( str(start_num%10) * (i+1) , end = " " )
    
    print()

print()