n1,n2,n3,n4=input().split()
n1,n2,n3,n4=float(n1),float(n2),float(n3),float(n4)
n1=n1*2
n2=n2*3
n3=n3*4
n4=n4*1
m=(n1+n2+n3+n4)/10.0
print("Media:",m)
if m>7.0 or m==7.0:
    print("Aluno aprovado.")
elif m<5.0:
    print("Aluno reprovado.")
elif m>=5.0 and m<=6.9:
    print("Aluno em exame.")
    e=float(input())
    print("Nota do exame: ",e)
    f=(m+e)/2
    print("Aluno aprovado.")
    if f>5.0 or f==5.0:
        print("Aluno reprovado.")
        print("Media final: ",f)