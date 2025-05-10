luong = float(input("Nhập lương nhân viên (triệu đồng): "))
if luong > 15:
    thue = luong * 0.3
elif luong >= 7:
    thue = luong * 0.2
else:
    thue = luong * 0.1
luong_rong = luong - thue
print(f"Thuế thu nhập: {thue:.2f} triệu đồng")
print(f"Lương ròng: {luong_rong:.2f} triệu đồng")

