n=int(input())
x=[3600,60]
a=n//x[0]
b=n//x[1]
if b>x[1]:
    b=b%x[1]
else:
    b=n//x[1]
c=n%x[1]
print(a,b,c,sep=":")