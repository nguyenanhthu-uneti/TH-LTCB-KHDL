luong = float(input("Nhập lương nhân viên (triệu VND): "))
if luong >= 15:
    thue = 0.30 * luong  # 30% thuế
elif 7 <= luong < 15:
    thue = 0.20 * luong  # 20% thuế
else:
    thue = 0.10 * luong  # 10% thuế

# lương ròng
luong_rong = luong - thue

#  kết quả
print(f"Thuế thu nhập: {thue:.2f} triệu VND")
print(f"Lương ròng (số tiền thực nhận): {luong_rong:.2f} triệu VND")