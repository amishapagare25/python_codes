t=int(input())
l=[]
result=0
for i in range(t):
    n=int(input())
    amount=list(map(int,input().split()))
    total=amount[0]
    for i in range(len(amount)-1):
        total=total+amount[i+1]
        l.append(total)
        result=result+total
    print(result)

