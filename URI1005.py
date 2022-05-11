A=float(input("Birinci puani girin: "))
B=float(input("İkinci puani girin: "))
A=A*3.5
B=B*7.5
Average=(A+B)/11.0
print("MEDIA: "+str(Average))
if Average>38:
    print("APPROVED")
else:
    print("NOT APPROVED")