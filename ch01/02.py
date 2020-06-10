#2

n = int( input("> ") )

for i in range( n ) :

    print( "sum([1," , n-i , "])" , " = " , end = "" , sep = "" )

    val = 0 

    for j in range( n-i-1 ) :

        val += j+1

        print( j+1 , end = "+" )
    
    print( n-i , "= " , end = "" )
    val += n-i
    print( val )

        