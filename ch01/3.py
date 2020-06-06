#3

n = int( input("> ") )

start_num = 0

for i in range( n ) :

    for j in range( n ) :

        start_num += 1

        print( start_num%10 , end = " " )
    
    print()