points=list(map(int,input().split()))
total=0
total2=0
total3=0
for i in range(points[1]):
    more=list(map(int,input().split()))
    total = total + more[2]

restaurants=int(input())
for i in range(restaurants):
    place = list(map(int, input().split()))
for i in range(points[1]):
    total2 = total- more[2]
print(total)
print(total2)
print(total3)


