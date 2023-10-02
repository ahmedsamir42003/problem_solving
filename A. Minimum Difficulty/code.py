n=int(input())
li=[int(i) for i in input().split()]
out=[]
for i in range(2,n):
    wr=li.copy()
    del wr[i-1]
    mx=[]
    for i in range(n-2):
        mx.append(wr[i+1]-wr[i])
    out.append(max(mx))
print(min(out))