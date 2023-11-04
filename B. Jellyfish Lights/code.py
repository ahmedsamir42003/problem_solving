x=int(input())
li=[int(i) for i in input()]
sum1=0
sum2=0
for i in range(len(li)):
    if (i+1)%2==0:
        if li[i]==0:
            sum1=sum1+1
    else:
        if li[i]==1:
            sum1=sum1+1

for i in range(len(li)):
    if (i+1)%2==0:
        if li[i]==1:
            sum2=sum2+1
    else:
        if li[i]==0:
            sum2=sum2+1

print(min(sum1,sum2))

