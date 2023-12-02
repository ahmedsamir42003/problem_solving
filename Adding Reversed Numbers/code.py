def re(x):
  xr=0
  for i in range(len(x)):
      xr=xr+ ( int('1'+i*'0')*int(x[i]) )
  return xr

n=int(input())
for i in range(n):
    x1,x2=input().split()
    x1r=re(x1)
    x2r=re(x2)
    print( re( str(x1r+x2r) ) )


