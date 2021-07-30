def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            return True
        i=i+1
    return False
list=[7,9,5,8]
n=5
if search(list,n):
    print("found")
else:
    print("not")
