def sqrt():
    s=1
    while s<=10:
        sq = s*s
        yield sq
        s=s+1
l=sqrt()
print(next(l))