stack=[]
def add():
    n=int(input())
    stack.append(n)
    print(stack)

def remove():
    if  len(stack)==0:
        print(len(stack))
        print("stack is full")
    else:
        stack.pop()
        print(stack)
while True:
    print("select 1.add 2.remove 3.quit")
    select=int(input())
    if 1==select:
        add()
    elif 2==select:
        remove()
    elif 3==select:
         quit()
    else:
        print("select right one na")
