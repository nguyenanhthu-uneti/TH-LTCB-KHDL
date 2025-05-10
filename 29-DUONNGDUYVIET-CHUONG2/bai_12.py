tnct = int(input("Nhập thâm niên công tác (tháng): "))
luong_co_ban = 1350000
if tnct < 12:
    he_so = 2.34
elif 12 <= tnct < 36:
    he_so = 3.33
elif 36 <= tnct < 60:
    he_so = 3.66
else:
    he_so = 3.99
luong = he_so * luong_co_ban
print(f"Thâm niên công tác: {tnct} tháng")
print(f"Hệ số lương: {he_so}")
print(f"Lương của nhân viên: {luong} VND")
