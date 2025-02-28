n = int(input("Nhập thâm niên công tác  : "))
luong_co_ban = 1350000
if n < 12:
    he_so = 2.34
elif 12 <= n < 36:
    he_so = 3.33
elif 36 <= n < 60:
    he_so = 3.66
elif  n >= 60:
    he_so = 3.99
luong = he_so * luong_co_ban
print(f"Lương nhân viên là :{luong}")