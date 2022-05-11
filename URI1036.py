A,B,C=input().split()
A,B,C=float(A),float(B),float(C)
D=B**2-4*A*C

if D<0 or A==0:
    print("Impossivel calcular")
else:
    R1=(-1*B+D**0.5)/(2*A)
    R2=(-1*B-D**0.5)/(2*A)
    print("R1 = {:.5f}".format(R1),"R2 = {:.5f}".format(R2),sep="\n")