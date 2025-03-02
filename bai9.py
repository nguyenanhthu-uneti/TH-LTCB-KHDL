luong = float(input("nhap luong nhan vien: "))

if luong >= 15000000:
    thue = 0.3
elif luong >= 7000000:
    thue = 0.2
else:
    thue = 0.1

thue_thu_nhap = luong * thue
luong_rong = luong - thue_thu_nhap

# Xuất kết quả
print(f"thue thu nhap: {thue_thu_nhap}")
print(f"luong rong: {luong_rong}")