xy=input()

a=xy[0:2]
b=list(a)
c=b.reverse()
d=''.join(b)
e=xy[3:5]
f=''.join(e)
g=int(d)-int(f)
if g>0:
   print(g)
else:
   h=60-int(f)
   i=int(d)+h
   print(i)