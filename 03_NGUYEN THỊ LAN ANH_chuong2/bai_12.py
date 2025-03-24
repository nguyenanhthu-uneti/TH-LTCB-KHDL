tnct = int(input("Nhap tham nien cua nhan vien: "))
luong_co_ban = 1350000
if tnct<12:
    he_so=2.34
elif tnct<=12 and tnct<36:
    he_so=3.33
elif tnct<=36 and tnct<60:
    he_so=3.66
else:
    he_so=3.99
luong=he_so*luong_co_ban
print(f"Voi tham nien cong tac {tnct} thang thi luong cua nhan vien la {luong}")