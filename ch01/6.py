#6

n = int( input("> ") )

start_num = 0 
inverse_start_num = (n-1) * 4 + 1

for i in range( n ) :

    start_num += 1
    print( start_num%10 , end = " " )

print()

for i in range( n-2 ) :

    inverse_start_num -= 1
    print( inverse_start_num%10 , end = " " )

    for j in range( n-2 ) :
        print( " " , end = " " )
    
    start_num += 1 
    print( start_num%10 )

for i in range( n ) :
    
    inverse_start_num -= 1
    print( inverse_start_num%10 , end = " " )

print()


