t=int(input())
for i in range(t):
    n=int(input("enter total"))
    m=int(input("sweets"))
    s=int(input("start"))
    if(((s-1)+m )%n==0):
        print( n);
    else:
        print ((((s-1)+m)%n)) ;





