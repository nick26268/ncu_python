#7

n = int( input("> ") )

start_num = 0

for i in range( n ) :

    print( 2 * " " * (n-i-1) , end = "" )
    for j in range( i+1 ) :

        start_num += 1
        print( start_num%10 , end = " " )
    
    print()

print()