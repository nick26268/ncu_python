# 9

n = int( input("> ") )

num = 0 

for i in range( n ) :

    for j in range( n ) :

        print( (i+j)%n+1 , end = " " )
    
    print()

print()