n = int(input("Nhập năm cần kiểm tra :"))
if n%4==0 and n%100!=0:
    print(f"{n}la nam nhuan")
elif n%400 ==0:
    print(f"{n} la nam nhuan")
else:
    print(f"{n} la nam nhuan")
