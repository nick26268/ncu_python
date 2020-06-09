#4

n = int( input("> ") )

start_num = 0 

for i in range( n ) :

    start_num += 1 
    print( start_num%10 , end = " " )

print()

for i in range( n-2 ) :

    start_num += 1 
    print( start_num%10 , end = " " )

    for j in range( n-2 ) :
        print( " " , end = " " )
    
    start_num += 1
    print( start_num%10 )

for i in range( n ) :
    
    start_num += 1 
    print( start_num%10 , end = " " )

print()