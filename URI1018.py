x=[100,50,20,10,5,2,1]

n=int(input())

lista=[]
for i in x:
    lista.append(n//i)
    n=n%i

print(n)

print(f'{lista[0]} nota(s) de R$ {x[0]:.2f}\n{lista[1]} nota(s) de R$ {x[1]:.2f}\n{lista[2]} nota(s) de R$ {x[2]:.2f}\n{lista[3]} nota(s) de R$ {x[3]:.2f}\n{lista[4]} nota(s) de R$ {x[4]:.2f}\n{lista[5]} nota(s) de R$ {x[5]:.2f}\n{lista[6]} nota(s) de R$ {x[6]:.2f}\n')