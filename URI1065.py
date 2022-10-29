a,b,c,d,e=(float(input()) for _ in range(5))
a,b,c,d,e=int(a),int(b),int(c),int(d),int(e)
l1=[a,b,c,d,e]
l2=[i for i in l1 if i%2==0]
print("%s valores pares"%len(l2))