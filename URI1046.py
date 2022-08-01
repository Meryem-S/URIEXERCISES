x,y=input().split()
x,y=int(x),int(y)

if x==y:
    time=24
    print("O JOGO DUROU %s HORA(S)"%(time))

elif x>12 or x<=24:
    if x<y:
        time=abs(x-y)
    elif x>y:
            time=(24-x)+y
    print("O JOGO DUROU %s HORA(S)"%(time))

elif x<=12 or x>=0:
    if x<y:
        time=abs(y-x)
    elif x>y:
        time=abs(24-x)+y
    print("O JOGO DUROU %s HORA(S)"%(time))