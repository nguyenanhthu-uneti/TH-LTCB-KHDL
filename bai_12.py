TNCT = int(input("thâm niên công tác(tháng):"))
luong_co_ban = 1350000
if TNCT < 12:
    he_so_luong = 2.34
elif 12 <= TNCT < 36:
    he_so_luong = 3.33
elif 36 <= TNCT < 60:
    he_so_luong = 3.66
else:
    he_so_luong = 3.99
luong = luong_co_ban * he_so_luong
print(f"Lương nhân viên là:",luong,"VND")