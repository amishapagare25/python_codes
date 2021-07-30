s = input()

def swapcase(s):
    result=""
    for i in s:
        if i==i.upper():
            result+=i.lower()
        else:
            result+=i.upper()
    return result

new=swapcase(s)
print(new)
