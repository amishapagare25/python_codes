t=int(input())
c=[]
for i in range(1,100):
    if i>1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
               c.append(i)
prime= sorted(list(set(c)))
lili=[]
ans=[]
for i in range(t):
    n=int(input())
    for i in prime:
        diff =abs(n-i)
        lili.append(diff)
        indexpos= lili.index(min(lili))
        answer=(prime[indexpos])
        ans.append(answer)
print(ans)









