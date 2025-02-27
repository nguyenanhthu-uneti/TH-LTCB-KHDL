luong_co_ban = 1350000
tnct_nhan_vien = int(input( " Nhap vao tham nien cong tac (so thang ): "))
if tnct_nhan_vien < 12:
    he_so = 2.34
elif 12 <= tnct_nhan_vien < 36:
    he_so = 3.33
elif 36 <= tnct_nhan_vien < 60:
    he_so = 3.66
else:
    he_so = 3.99
luong_nhan_vien = he_so * luong_co_ban
print("Luong cua nhan vien la ", luong_nhan_vien,"dong")
