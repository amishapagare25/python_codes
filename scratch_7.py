a=int(input())
b=int(input())
li=[]
counter=0
samples= list(map(int, input().split()))
samples.sort()
#print(samples)
for i in range(0,a):
	ranges=list(map(int, input().split()))
	for j in range(0,b):
		if samples[j]>ranges[0] and samples[j]<ranges[1]:
			counter=counter+1
	li.append(counter)
	#print(counter)
	counter=0
print(li)