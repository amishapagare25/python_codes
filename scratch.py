n=list(map(int,input().split()))
arr=list(map(int,input().split()))
arr3=list(reversed(sorted(arr)))
arr2=len(arr3)
count=0
for i in range(arr2):
    for j in range(i,arr2):
        if (arr3[i]-arr3[j]==n[1]):
            count=count+1
        else:
            continue
print(count)