n=int(input())
li=[int(i) for i in input().split()]
li=sorted(li,reverse=True)
goal=0
if sum(li)<n:
    print(-1)
    exit()
for i in range(12):
    if goal < n:
        goal=goal+li[i]
    else:
        print(i)
        exit()
print(12)