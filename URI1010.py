code1,num1,price1 = input("Enter code, number and price of product 1 space-separated\n").split()
code2,num2,price2 = input("Enter code, number and price of product 2 space-separated\n").split()
pay=int(num1)*float(price1)+int(num2)*float(price2)
print("Value to Pay:$ {:.2f}".format(pay))