#22

n = int( input("> ") )

print( "1" , "-" * ( 4 * n - 5 ) , "2" , "-" * ( 4 * n - 5 ) , "3" , sep = "" )

start_num = 3 

for i in range( n-2 ) :

    start_num += 1

    print( " " * ( i+1 ) * 2 , start_num%10 , sep = "" , end = "" )

    start_num += 1

    print( "-" * ( 4 * n - 5 - 4 * (i+1) ) , start_num%10 , sep = "" , end = "" )

    print( " " * ( 3 + 2 * i ) , end = "" )

    start_num += 1

    print( " " * i * 2 , start_num%10 , sep = "" , end = "" )

    start_num += 1

    print( "-" * ( 4 * n - 5 - 4 * (i+1) ) , start_num%10 , sep = "" , end = "" )

    print()

start_num += 1

print( 2 * " " * ( n - 1 ) , start_num % 10 , sep = "" , end = "" )

start_num += 1

print( ( 4 * n - 5 ) * " " , start_num%10 , sep = "" )

print()


    


