thang = int(input("Nhap thang: "))
if thang==2:
    nam = int(input("Nhap nam: "))
    if (nam%4==0 and nam%100!=0) or nam%400==0:
        print(f"Thang {thang} co 29 ngay")
    else:
        print(f"Thang {thang} co 28 ngay")
elif thang%2!=0 or thang == 8:
    print(f"Thang {thang} co 31 ngay")
else:
    print(f"Thang {thang} co 30 ngay")