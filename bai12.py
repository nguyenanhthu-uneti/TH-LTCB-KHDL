tnct=int(input("nhập số tháng công tác :"))
if tnct < 12 :
    he_so = 2.34
elif tnct < 36 :
    he_so=3.33
elif tnct < 60 :
    he_so = 3.66 
else:
    he_so = 3.99
luong_co_ban = 1350000
luong=he_so * luong_co_ban
print(f"lương của nhân viên : {luong:.0f} dong")