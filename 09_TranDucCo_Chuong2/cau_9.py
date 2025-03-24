luong_nhan_vien = float(input("Nhập số lương của nhân viên: "))
if luong_nhan_vien >= 15000000:
    phi_thue = 0.3
elif luong_nhan_vien >= 7000000  and luong_nhan_vien < 15000000:
    phi_thue = 0.2
elif luong_nhan_vien < 7000000:
    phi_thue = 0.1   
tien_thue = luong_nhan_vien*phi_thue 
luong_thuc_te = luong_nhan_vien - tien_thue
print(f'Thuế thu nhập của nhân viên là: {tien_thue}')
print(f'Lương thực tế của nhân viên là:{luong_thuc_te}')