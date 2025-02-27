thang=int(input("Nhap thang: "))
nam=int(input("Nhap nam: "))   
if thang==1 or thang==3 or thang==5 or thang==7 or thang==8 or thang==10 or thang==12:
    print(f"Thang {thang} co 31 ngay")
elif thang==2:
    if nam%4==0 and nam%100!=0 or nam%400==0:
        print(f"Thang {thang} co 29 ngay")
    else:
        print(f"Thang {thang} co 28 ngay")
else:
    print(f"Thang {thang} co 30 ngay")