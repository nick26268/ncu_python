#1

nitr = 0

for num in range(100,1000) :

	#百位數
	x = num//100

	#十位數
	y = num%100//10

	#個位數
	z = num%100%10

	if( x+y+z == 10 and x != y != z != x ) :

		nitr += 1

		print( "{:>2}".format(nitr) , ":" , num )

print( "\n" , "總共",nitr,"個" , sep = "" )