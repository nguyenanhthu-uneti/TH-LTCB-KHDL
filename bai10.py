n= int(input("nhap thang :"))
if n ==2 :
    print(" thang 2 co 28 ngay hoac 29 ngay neu la nam nhuan")
elif n in [1,3,5,7,8,10,12]:
    print ("thang {n} co 31 ngay")
elif n in [4,6,9,11]:
    print ("thang {n} co 30 ngay")
else:
    print(" ban can nhap lai")