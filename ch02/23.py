#23

n = int( input("請輸入奇數> ") )

for i in range( 2*n-1 ) :

    for j in range( 3*n-2 ) :

        if j-i == 0 or i+j == 2*n-2 or j-i == 2*n-2 or i+j == 3*n-3 and i <= n-1 or j-i == n-1 and i > n-1 or i+j == 4*n-4 :

            print( "*" , end = " " )

        else :

            print( " " , end = " " )

    print() 