house=list(map(int,input().split()))
total=0
for i in range(len(house)):
    if i%2==0:
        total=total+house[i]
print(total)