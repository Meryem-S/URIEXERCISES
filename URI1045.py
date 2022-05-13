A,B,C=input().split()
A,B,C=float(A),float(B),float(C)
nums=[A,B,C]
nums.sort()
nums.reverse()
A=(A%2==0 and A>0)
B=(B%2==0 and B>0)
C=(C%2==0 and C>0)
A=nums[0]
B=nums[1]
C=nums[2]

if A>=(B+C):
    print("NAO FORMA TRIANGULO")
else:
    if (A**2)==((B**2)+(C**2)):
        print("TRIANGULO RETANGULO")
    elif (A**2)>((B**2)+(C**2)):
        print("TRIANGULO OBTUSANGULO")
    elif (A**2)<((B**2)+(C**2)):
        print("TRIANGULO ACUTANGULO")
if A==B==C:
    print("TRIANGULO EQUILATERO")
if (A==B and A!=C) or (A==C and A!=B) or (C==B and C!=A):
    print("TRIANGULO ISOSCELES")