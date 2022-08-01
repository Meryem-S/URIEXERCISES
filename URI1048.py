s=float(input())
rate=[15,12,10,7,4]
if s>0 and s<=400.00:
    e_p=rate[0]
    n_s=s+(s*e_p/100)
    r_g=n_s-s
elif s>=400.01 and s<=800.00:
    e_p=rate[1]
    n_s=s+(s*e_p/100)
    r_g=n_s-s
elif s>=800.01 and s<=1200.00:
    e_p=rate[2]
    n_s=s+(s*e_p/100)
    r_g=n_s-s
elif s>=1200.01 and s<=2000.00:
    e_p=rate[3]
    n_s=s+(s*e_p/100)
    r_g=n_s-s
else:
    e_p=rate[4]
    n_s=s+(s*e_p/100)
    r_g=n_s-s
print("Novo salario: {:.2f}".format(n_s)+"\n"+"Reajuste ganho: {:.2f}".format(r_g)+"\n"+"Em percentual: "+str(e_p)+" %")
