n = int(input("nhap nam: "))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print(" la nam nhuan")
else:
    print(" khong phai la nam nhuan")
