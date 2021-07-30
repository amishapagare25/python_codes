time=list(input())
m=(time[0:2])
ms=''.join(map(str,m))
s=(time[3:5])
ss=''.join(map(str,s))
if((int(ms)<=24) & (int(ss)<=60)):
    rev =(ms[: :-1])
    diff=int(rev)-int(ss)
    if(diff < 0):
        print(diff*(-1))
    else:
        print(diff)
