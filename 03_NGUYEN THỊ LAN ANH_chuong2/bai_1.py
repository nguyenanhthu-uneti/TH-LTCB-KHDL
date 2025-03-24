n = int(input("Nhap nam: "))
if (n%4==0 and n%100!=0) or n%400==0:
    print(f"{n} la nam nhuan")
else:
    print(f"{n} khong la nam nhuan")