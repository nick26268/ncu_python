#21

n = int( input("> ") )

sum = 0

for i in range( n-1 ) :

    print( " " * 2 * i , end = "" )
    
    sum += 1 

    print( sum%10 , end = "" )

    print( "-" * (4 * n - 5 - 4 * i ) , end = "" )

    sum += 1

    print( sum%10 )

sum += 1

print( " " * 2 * ( n-1 ) , sum%10 , sep = "" )

print()
