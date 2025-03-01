luong = float(input("Nhập lương của nhân viên: "))
thue = 0
luong_rong = 0
if luong >= 15000000:
    thue = luong * 0.3
elif luong >= 7000000 and luong < 15000000:
    thue = luong * 0.2
else: 
    thue = luong * 0.1
luong_rong = luong - thue
print(f"Lương:{luong}.đồng")
print(f"Thuế:{thue}.đồng")
print(f"Lương ròng:{luong_rong}.đồng")
