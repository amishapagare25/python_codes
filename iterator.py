class eleven:
    def __init__(self):
        self.m=4
    def __iter__(self):
        return self
    def __next__(self):
        if self.m<11:
         val=self.m
         self.m+=1
         return val
        else:
            raise StopIteration
e=eleven()
print(e.__next__())
for i in e:
    print (i)