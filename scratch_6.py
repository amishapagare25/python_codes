sr=list(map(int,input().split()))
r=sr[1]
count=0
li=[]
samples=list(map(int,input().split()))
for i in range(r):
    between=list(map(int,input().split()))
    for j in samples:
        if(between[0]<j<between[1]):
            count=count+1
    li.append(count)
    count=0
print(li)