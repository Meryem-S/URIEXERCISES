a=float(input())
x=[0,8,18,28]
f=a-4500
g=a-3000
h=a-2000
    
if a<=2000:
    print("Isento")
else:
    if a>=2000.01 and a<=3000:
        vergi=(h*x[1]/100)+(g*x[2]/100)
    elif a>=3000.01 and a<=4500:
        vergi=(g*x[2]/100)+((h-g)*x[1]/100)
    else:
        vergi=(f*x[3]/100)+((h-g)*x[1]/100)+((g-f)*x[2]/100)
    print("R$ {:.2f}".format(vergi))