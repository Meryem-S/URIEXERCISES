a=float(input())
x=[100,50,20,10,5,2]
y=[1,0.50,0.25,0.10,0.05,0.01]
list_1=[]
list_2=[]

for i in x:
    list_1.append(a//i)
    a=a%i

print("NOTAS:"+"\n",list_1[0],"nota(s) de R$",'%.2f' % x[0],"\n",list_1[1],"nota(s) de R$",'%.2f' % x[1],"\n",list_1[2],"nota(s) de R$",'%.2f' % x[2],"\n",list_1[3],"nota(s) de R$",'%.2f' % x[3],"\n",list_1[4],"nota(s) de R$",'%.2f' % x[4],"\n",list_1[5],"nota(s) de R$",'%.2f' % x[5])

for j in y:
    list_2.append(a//j)
    a=a%j

print("MOEDAS:"+"\n",list_2[0],"nota(s) de R$",'%.2f' % y[0],"\n",list_2[1],"nota(s) de R$",'%.2f' % y[1],"\n",list_2[2],"nota(s) de R$",'%.2f' % y[2],"\n",list_2[3],"nota(s) de R$",'%.2f' % y[3],"\n",list_2[4],"nota(s) de R$",'%.2f' % y[4],"\n",list_2[5],"nota(s) de R$",'%.2f' % y[5])