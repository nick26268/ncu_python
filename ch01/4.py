#4

n = int( input("> ") )

start_num = 0 

for i in range( n ) :

    start_num += 1 
    print( start_num%10 , end = " " )

print()

for i in range( n-2 ) :

    for j in range( n ) :
        
        if ( j == 0 or j == n-1 ) :
            
            start_num += 1
            print( start_num%10 , end = " " )
        
        else :
            print( " " , end = " " )
    
    print()

for i in range( n ) :
    
    start_num += 1 

    print( start_num%10 , end = " " )

print()