A,B,C=input().split()
A,B,C=float(A),float(B),float(C)
p=A+B+C
a=((A+B)*C)/2
if (A+B)>C and (A+C)>B and (B+C)>A:
    print("Perimetro =",p)
else:
    print("Area =",a)