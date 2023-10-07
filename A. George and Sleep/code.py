import time

gitup=input()
numh=input()

gh,gm=[int (i) for i in gitup.split(':')]
nh,nm=[int (i) for i in numh.split(':')]

for i in range(nh):
    if gh==0:
        gh=23
    else:
        gh=gh-1

for i in range(nm):
    if gm==0:
        if gh==0:
            gh=23
            gm=59
        else:
            gh=gh-1
            gm = 59
    else:
        gm=gm-1

if gh<10 and gm<10:
    print('0'+str(gh)+':'+'0'+str(gm))
elif gh<10 and gm>=10:
    print('0' + str(gh) + ':' +str(gm))
elif gh>=10 and gm<10:
    print(str(gh) + ':' + '0' + str(gm))
else:
    print(str(gh) + ':' +str(gm))