x, y, z, a, b, c = (float(input()) for _ in range(6))
l1=[x,y,z,a,b,c]
l2=[e for e in l1 if e>0]
print("%s valores positivos"%len(l2))

