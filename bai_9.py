luong = float(input("Nhập lương nhân viên: "))
if luong >= 15000000:
    thue = 0.3
elif luong >= 7000000:
    thue = 0.2
else:
    thue = 0.1
thue_thu_nhap = luong * thue
luong_rong = luong - thue_thu_nhap
print(f"thuế thu nhập: {thue_thu_nhap}")
print(f"lương ròng: {luong_rong}")