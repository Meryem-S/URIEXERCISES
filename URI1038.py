X,Y=input().split()
X,Y=int(X),int(Y)
p=[1,4.00,4.50,5.00,2.00,1.50]
for i in range(6):
    if X==i:
        Y=p[i]*Y       
total=Y
print("Total: R$ {:.2f}".format(total))