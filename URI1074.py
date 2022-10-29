N=int(input())
numbers= []
for x in range (N):
    n=int(input())
    numbers.append(n)
for i in numbers:
    if i%2==0 and i<0:
        print("EVEN NEGATIVE")
    elif i%2==0 and i>0:
        print("EVEN POSITIVE")
    elif i==0:
        print("NULL")
    elif i%2==1 and i<0:
        print("ODD NEGATIVE")
    else:
        print("ODD POSITIVE")
        