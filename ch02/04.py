#4
for num in range( 10000 , 100000 ):
    ch1 = num//10000 #學
    ch2 = num%10000//1000 #習 
    ch3 = num%1000//100 #再
    ch4 = num%100//10 #學
    ch5 = num%10 #習

    if( ch1 == ch4 and ch2 == ch5 ) :

        ans = num * ch4 
        ans = str(ans)
        if( len(ans) ==6 ) :
            pass 
        else :
            continue

        if( ans[0]==ans[1] and ans[1]==ans[2] and ans[2]==ans[3] and ans[3]==ans[4] and ans[4]==ans[5] ) :

            print( " " , " " , " " , ch1 , ch2 , ch3 , ch4 , ch5 )
            print( " " , "X" , " " , " " , " " , " " , " " , ch1 )
            print( "_"*16 )
            print( " " , " " , ans[0] , ans[1] , ans[2] , ans[3] , ans[4] , ans[5] )
            
            