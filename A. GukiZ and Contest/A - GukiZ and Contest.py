ns=int(input(''))
li=[int(i) for i in input().split()]

my_dict={}

for i in range(len(li)):
    my_dict[i]=li[i]


my_dict = sorted(my_dict, key=lambda x: my_dict[x], reverse=True)

li=sorted(li,reverse=True)



order=0
out={}
score=-1
n=0

for i in range(len(li)):

    if li[i]==score:
        n = n+1
        out[my_dict[i]]=order
    else:
        order=(order+1)+n
        out[my_dict[i]] = order
        score=li[i]
        n = 0

out = dict(sorted(out.items()))

li=list(out.values())

for i in li:
    print(i,end=" ")