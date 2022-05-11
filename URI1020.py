a=int(input())
b=a//365
c=(a%365)//30
d=(a%365)%30
print(str(b)+" "+"ano(s)",str(c)+" "+"mes(es)",str(d)+" "+"dia(s)",sep="\n")