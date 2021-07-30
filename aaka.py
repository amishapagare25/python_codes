s=list(map(str,input()))
n=len(s)
k=int(input())
r=k
x=0
if((n%k)==0):
    for i in range(n):
        li= set(list(s[x:k]))
        tostr=''.join(map(str,li))
        print(tostr)
        x=x+r
        k=k+r


