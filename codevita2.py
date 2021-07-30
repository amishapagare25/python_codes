n=int(input())
l=[]
total=0
c=0
for i in range(2,n):
    print(i)
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            l.append(i)
for i in l:
    total=total+i
    if total in l:
        c=c+1
print(c-1)