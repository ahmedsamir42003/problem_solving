import math
p, zp, d, zd = [int(i) for i in input().split()]
if p > d:
    print(p)
    exit()
n1=math.floor((d - p) / (zd + zp))
n2=math.ceil((d - p) / (zd + zp))
if (d-zd* n1) > (p + zp * n1) and  (d-zd* n1) < (p + zp * n2) :
    print(d-zd* n1)
elif (p + zp * n1)>=( d-zd* n1):
    print(p + zp * n1)
else:
    print(p + zp * n2)

