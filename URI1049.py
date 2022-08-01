x=input()
y=input()
z=input()
list_1=["vertebrado","invertebrado"]
list_2=["ave","mamifero","inseto","anelideo"]
list_3=["carnivoro","onivoro","herbivoro","hematofago"]
list_4=["aguia","pomba","homem","vaca","pulga","lagarta","sanguessuga","minhoca"]
if x==list_1[0]:
    if y==list_2[0]:
        if z==list_3[0]:
            print(list_4[0])
        elif z==list_3[1]:
            print(list_4[1])
    elif y==list_2[1]:
        if z==list_3[1]:
            print(list_4[2])
        elif z==list_3[2]:
            print(list_4[3])

elif x==list_1[1]:
    if y==list_2[2]:
        if z==list_3[3]:
            print(list_4[4])
        elif z==list_3[2]:
            print(list_4[5])
    elif y==list_2[3]:
        if z==list_3[3]:
            print(list_4[6])
        elif z==list_3[1]:
            print(list_4[7])