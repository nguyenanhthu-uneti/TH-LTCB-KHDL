a=int(input("Nhap nam: "))
if a%4==0 and a%100!=0 or a%400==0:
    print(f"Nam {a} la nam nhuan")
else:
    print("Nam {a} khong la nam nhuan")