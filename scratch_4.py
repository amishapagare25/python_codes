import textwrap
def merge_the_tools(string, k):
    part=int(len(string)/k)
    a1=textwrap.wrap(string, k)
    for i in range((part)):
        sse1=set()
        for j in range(len(a1[i])):
               if a1[i][j] not in sse1:
                sse1.add(a1[i][j])
                print(a1[i][j],end="")
print()