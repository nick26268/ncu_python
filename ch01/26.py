#26

n = int( input("> ") )

for i in range( n ) :

    for k in range( n ) :

        print( " " * (n-i-1) , end = "" )

        for j in range( i+1 ) :

            print( "/\\" , end = "" )

        print( " " * (n-i-1) , end = "" ) 
    
    print()

print( "-" * n * n * 2 ) 

for i in range( n-1 , -1 , -1 ) :

    for k in range( n ) :

        print( " " * (n-i-1) , end = "" )

        for j in range( i+1 ) :

            print( "\\/" , end = "" )

        print( " " * (n-i-1) , end = "" ) 
    
    print()

print()