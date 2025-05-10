n = int(input("Nhap nam n: "))
if n%4 == 0 and n%100 != 0:
    print(f"nam {n} la nam nhuan.")
elif n%400 == 0:
    print(f"nam {n} la nam nhuan")
else:
    print(f"nam {n} khong la nam nhuan.")


