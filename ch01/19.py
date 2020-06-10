#19

n = int( input("> ") )

num = 1

for i in range( n ) :

    num += i

    for j in range( n ) :

        for s in range( i+1 ) :

            for t in range( n ) :

                print( (num+s)%10 , end = "" )
        
            print( " " , end = "" )
        
        print()
    
    print()

print()
    
