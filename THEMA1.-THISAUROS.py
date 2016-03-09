import random
row=[i for i in range(1,11)]
column=[j for j in range(1,11)]

board=[]
for i in row:
    for j in column:
        board.append([i,j])


tmp=board
random.shuffle(tmp)




pc=[tmp[0]]
user=[tmp[1]]
print "Vriskesai edw", user


#ksexwrizw sthlh-gramh pinaka,gia na ta xrhsimopoihsw meta(pc).
r=pc.pop()
pc2=r.pop()
pc1=r.pop()
pc=[pc1,pc2]
#to idio me prin alla gia ton user.
e=user.pop()
user2=e.pop()
user1=e.pop()



while cmp(user,pc)>0 or cmp(user,pc)<0:

    a = raw_input("Pros ta pou thes na pas?Up->U,Down->D,Right->R.Left->L")

    if a=="U" and user1>1:
        user=[user1-1,user2]
        user1=user1-1
        print "metaferthikes edw",user
    elif a=="D" and user1<10:
        user=[user1+1,user2]
        user1=user1+1
        print "metaferthikes edw",user
    elif a=="R" and user2<10:
        user=[user1,user2+1]
        user2=user2+1
        print "metaferthikes edw",user
    elif a=="L" and user2>1:
        user=[user1,user2-1]
        user2=user2-1
        print "metaferthikes edw",user
    else:
        print "edwses lathos apanthsh"
    #Up-Down apostasth
    if pc1>user1:
        apost1=pc1-user1
    elif user1>pc1:
        apost1=user1-pc1
    else:
        apost1=0

    #Right-Left apostash
    if pc2>user2:
        apost2=pc2-user2
    elif user2>pc2:
        apost2=user2-pc2
    else:
        apost2=0

    #sunolikh Apostash
    sum1=apost1+apost2
    print "apostash thisaurou-paixth:",sum1

if cmp(user,pc)==0:
    print "Vrikes ton thisauro,The End"
    



