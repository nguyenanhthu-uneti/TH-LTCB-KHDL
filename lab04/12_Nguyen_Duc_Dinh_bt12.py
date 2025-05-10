luong = 1350000
tham_nien_cong_tac = int(input("Nhập số tháng đã công tác tại nơi này: "))
if tham_nien_cong_tac < 12:
    luong_moi = luong * 2.34
elif tham_nien_cong_tac < 36:
    luong_moi = luong * 3.33
elif tham_nien_cong_tac < 60:
    luong_moi = luong * 3.66
else:
    luong_moi = luong * 3.99
print(f"lương tháng là: {luong_moi}")
