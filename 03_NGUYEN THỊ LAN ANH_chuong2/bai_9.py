luong = int(input("Nhap luong cua nhan vien: "))
if luong >= 15000000:
    thue=0.3
elif luong >= 7000000 and luong < 15000000:
    thue=0.2
else:
    thue=0.1
thue_thu_nhap=luong*thue
luong_rong=luong-thue_thu_nhap
print(f"Thue thu nhap la {thue_thu_nhap}")
print(f"Luong rong la {luong_rong}")