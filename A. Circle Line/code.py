n=int(input())
li=[int(i) for i in input().split()]
f,l=[int(i) for i in input().split()]

if f==l:
    print(0)
    exit()
fs=0

if f < l:
    fs=l-f
elif  f == n:
    fs=l
else:
    fs=(n-f)+l

sum1=0
steps=0
i=f-1
while steps < fs:
    sum1=sum1+li[i]
    steps=steps+1
    if i == n-1:
        i = 0
    else:
        i=i+1

fl=0
if f < l:
    fl=(n-(l-f))
else:
    fl=f-l

sum2=0
steps=0
i=-(n-(f-1))

if i == -n:
    i = -1
else:
    i=i-1

while steps < fl:
    sum2=sum2+li[i]
    steps=steps+1
    if i == -n:
        i = -1
    else:
        i = i - 1

print(min(sum1,sum2))