def sort(lisst):
    for i in range(0,4):
        min=i
        for j in range(i,4):
            if lisst[j]<lisst[min]:
                min=j
        temp=lisst[i]
        lisst[i]=lisst[min]
        lisst[min]=temp
lisst=[7,2,9,1]
sort(lisst)
print(lisst)

