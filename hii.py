total=int(input())
scores = list(map(int, input().split()))
test_score= list(set(scores))
man=int(input())
man_score = list(map(int, input().split()))
man_scores=len(man_score)
for i in range(man_scores):
	j = man_score[i]
	test_score.append(man_score[i])
	scores2=list(reversed(sorted(test_score)))
	ini= scores2.index(j)
	ini+=1
	print(ini)









