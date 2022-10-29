X=int(input())
Y=int(input())
l=[]
for i in range(Y+1,X):
    if i%2==1:
        l.append(i)
total=sum(l)
print(total)