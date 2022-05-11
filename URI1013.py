A,B,C=input().split()
A,B,C=int(A),int(B),int(C)
greatest=int(A+B+abs(A-B))/2
if greatest<C:
    greatest=C
    print(greatest,"greatest number")