#3

num_1 , num_2 = eval( input("> ") )

num_1_len = len(str(num_1))
num_2_len = len(str(num_2))
col_len = len(str(num_1*num_2))+1


print( "\n" , " "*(col_len-num_1_len) , num_1 , sep="" )
print( "x" , " "*(col_len-num_2_len-1) , num_2 , sep="" )
print( "-"*(col_len) )

for index in range( num_2_len ) :

    ans = int(str(num_2)[num_2_len-index-1]) * num_1

    if( ans == 0 ) : continue

    print( " "*(col_len-len(str(ans))-index) , ans , sep = "" )

print( "-"*(col_len) )
print( " " , num_1 * num_2 , sep = "" )
