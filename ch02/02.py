#2

for num in range( 2 , 100 ) :

    print( num , end = " = " )

    for x in range( 2 , num+1 ) :

        

        while( num/x == num //x ) :

            num /= x
            
            if num == 1 : 
                print( x , end = "" )
                break 
            
            print( x , end = " x " )
        
        if num == x : 
            
            print( num , end = " " )
    
    print()
