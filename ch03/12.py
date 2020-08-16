#12

n = int( input("請輸入奇數> ") )

for i in range( n ) :

    for s in range( 3 ) :

        for j in range( n ) :

            for t in range( 3 ) :

                if j-i == 0 or j+i == n-1 :

                    print( n , end = "" )

                else :

                    print( " " , end = "" ) 
        
        print()

    