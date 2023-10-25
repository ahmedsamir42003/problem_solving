n,x=[int(i) for i in input().split()]
sum=0
for i in range(1,n+1):
    if x%i==0 and x/i <= n:
        sum=sum+1
print(sum)