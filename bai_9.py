luong = int(input(" Nhap luong cua nhan vien: "))
if luong >= 15000000:
    thue = 0.3
elif 7000000 <= luong <= 15000000:
    thue = 0.2
else :
    thue = 0.1
thue_thu_nhap= luong * thue
luong_rong = luong - thue_thu_nhap
print(f"thue thu nhap phai nop { thue_thu_nhap:.2f} ")
print(f"luong thuc nhan duoc la: {luong_rong:.2f}")
