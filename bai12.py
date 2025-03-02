tnct = int(input("nhap tham nien cong tac "))
if tnct  <12:
    luong = 2.34* 1350000
    print(luong)
elif  12 <= tnct < 36:
    luong = 3.33 * 1350000
    print(luong)
elif 36 <= tnct <60:
    luong = 3.66 * 1350000
    print(luong)
else:
    luong = 3.99 * 1350000
    print(luong)
    