n=list(map(int,input().split()))
num =n[0]
pr=n[1]
fac=[]
for i in range(1,num+1):
    if num%i==0:
        fac.append(i)
g=fac[::-1]
if len(g)>pr:
    print(g[pr-1])
else:
    print("1")
