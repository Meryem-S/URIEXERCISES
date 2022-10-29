X=int(input())
l=[]
for i in range(X+1):
    l.append(i)
    if l[i]%2==1:
        print(i)