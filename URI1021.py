a=float(input())
x=[100,50,20,10,5,2]
y=[1,0.50,0.25,0.10,0.05,0.01]
list_1=[]
list_2=[]


def money(list,kopek,money_type, total_money):
    for i in kopek:
        list.append(total_money//i)
        total_money=total_money%i

    print(money_type,":"+"\n",list[0],"nota(s) de R$",'%.2f' % kopek[0],"\n",list[1],"nota(s) de R$",'%.2f' % kopek[1],"\n",list[2],"nota(s) de R$",'%.2f' % kopek[2],"\n",list[3],"nota(s) de R$",'%.2f' % kopek[3],"\n",list[4],"nota(s) de R$",'%.2f' % kopek[4],"\n",list[5],"nota(s) de R$",'%.2f' % kopek[5])
    print(total_money) # how much money i still have to gave
    return total_money


rest=money(list_1,x,"NOTAS", a)

if rest != 0:
    money(list_2,y,"COINS", rest)