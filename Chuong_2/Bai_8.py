luong = float(input("Nhap luong cua nhan vien: "))
if luong >= 15000000:
    thue = 0.3
if luong >= 7000000:
    thue = 0.2
else:
    thue = 0.1
thue_thu_Nhap = luong * thue
luong_rong = luong - thue_thu_Nhap
print("thue thu nhap la:", thue_thu_Nhap)
print("luong rong la:", luong_rong)
