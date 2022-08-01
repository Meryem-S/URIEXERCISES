def average(L):
    total = 0
    for j in l2:
        total += j
        Average=round((total/len(L)),1)
    print(Average)
x, y, z, a, b, c = (float(input()) for _ in range(6))
l1=[x,y,z,a,b,c]
l2=[e for e in l1 if e>0]
print("%s valores positivos"%len(l2))
average(l2)