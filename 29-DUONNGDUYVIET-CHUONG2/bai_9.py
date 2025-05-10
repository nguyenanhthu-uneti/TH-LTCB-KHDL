luong = float(input("Nhập lương của nhân viên: "))
if luong <= 5000000:
    thue = 0
elif luong <= 10000000:
    thue = luong * 0.1
elif luong <= 18000000:
    thue = luong * 0.2
else:
    thue = luong * 0.3
luong_rong = luong - thue
print(f"Lương nhân viên: {luong} VND")
print(f"Thuế thu nhập: {thue} VND")
print(f"Lương ròng (sau thuế): {luong_rong} VND")
