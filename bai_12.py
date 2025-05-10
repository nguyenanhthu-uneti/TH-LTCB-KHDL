luong_co_ban = 1350000
tnct = int(input("nhap so thang tham nien"))
if tnct < 12:
                  he_so = 2.34
elif 12 <= tnct <= 36:
                  he_so = 3.33
elif 36 <= tnct <= 60:
                  he_so = 3.66
else:
                  he_so = 3.99
luong = he_so * luong_co_ban
print(f"luong cua nhan vien la {luong}")