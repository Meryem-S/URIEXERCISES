x,z,y,t=input().split()
x,z,y,t=int(x),int(z),int(y),int(t)
if x==y:
    hora=24
    if z==t:
        minuto=0
    elif z<t:
        minuto=(t-z)
    print("O JOGO DUROU %s HORA(S) E %s MINUTO(S)"%(hora,minuto))

elif x>12 or x<=24 and z<t:
    minuto=(t-z)
    if x<y:
        hora=abs(x-y)
    elif x>y:
        hora=(24-x)+y
    print("O JOGO DUROU %s HORA(S) E %s MINUTO(S)"%(hora,minuto))

elif x<=12 or x>=0 and z<t:
    minuto=t-z
    if (y-x)==1 and (z-t)==1:
        minuto=59
        hora=0
    elif x<y:
        hora=y-x
    elif x>y:
        hora=abs(24-x)+y
    print("O JOGO DUROU %s HORA(S) E %s MINUTO(S)"%(hora,minuto))