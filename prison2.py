t = int(input())
for i in range(t):
    n = list(map(int,input("enter").split()))
    if (((n[2] - 1) + n[1]) % n[0] == 0):
        print(n);
    else:
        print((((n[2] - 1) + n[1]) % n[0]));
