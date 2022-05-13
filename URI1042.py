x,y,z=input().split()
x,y,z=int(x),int(y),int(z)
if x<y:
    if x<z:
        if y<z:
            print(x,y,z,sep="\n")
        elif z<y:
            print(x,z,y,sep="\n")  
if y<x:
    if y<z:
        if x<z:
            print(y,x,z,sep="\n")
        elif z<x:
            print(y,z,x,sep="\n")
if z<x:
    if z<y:
        if y<x:
            print(z,y,x,sep="\n")
        elif x<y:
            print(z,x,y,sep="\n")
print("")
print(x,y,z,sep="\n")