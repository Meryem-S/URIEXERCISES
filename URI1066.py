a,b,c,d,e=(input() for _ in range(5))
a,b,c,d,e=int(a),int(b),int(c),int(d),int(e)
l1=[a,b,c,d,e]
l2=[i for i in l1 if i%2==0]
l3=[i for i in l1 if i%2==1]
l4=[i for i in l1 if i>0]
l5=[i for i in l1 if i<0]
print("%s valor(es) par(es)\n%s valor(es) impar(es)\n%s valor(es) positivo(s)\n%s valor(es) negativo(s)"%(len(l2),len(l3),len(l4),len(l5)))