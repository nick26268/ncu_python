#1

n = int( input("> ") )

for i in range( n ) :

    print( i+1 , end = "! = " )
    
    val = 1
    
    for j in range( i ) :
        val *= j+1
        print( j+1 , end= "x" )
    

    print( i+1 , end = " = " )
    val *= i+1
    print(val)