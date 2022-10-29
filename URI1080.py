list=[]
for i in range(100):
    x=int(input())
    list.append(x)
print(max(list))
print((list.index(max(list)))+1)