tnct = int(input("nhap tham nien cong tac:"))
if tnct < 12:
    luong = 2.34 * 1350
    print(f"luong la {luong}")
elif tnct >= 12 and tnct < 36:
    luong = 3.33 * 1350
    print(f"luong la {luong}")
elif tnct >= 36 and tnct < 60 :
    luong = 3.66 * 1350
    print(f"luong la {luong}")
else:
    luong = 3.99 * 1350
    print(f"luong la {luong}")
