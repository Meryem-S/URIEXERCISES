N=int(input())
inlist=[]
outlist=[]
for i in range(N):
    X=int(input())
    if X>=10 and X<=20:
        inlist.append(X)
    else:
        outlist.append(X)
    i+=1
print("%s in"%len(inlist)+str("\n")+"%s out"%len(outlist))