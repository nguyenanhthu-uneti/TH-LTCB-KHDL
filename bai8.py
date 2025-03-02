print("chương trình tính thu nhập(lương ròng)của nhân viên.")
luong = float(input("nhập lương của nhân viên:"))
if luong <=7000000:
    thue_suat=10
    tien_thue=luong*0.1
elif luong <=15000000:
    thue_suat=20
    tien_thue=luong*0.2
else:
    thue_suat=30
    tien_thue=luong*0.3
luong_rong = luong - tien_thue
print("lương nhân viên: %0.2f"%luong,'VND/tháng')
print("thuế suất là %d"%thue_suat,"%")
print("tiền lương thực nhận là: %0.2f"%luong_rong,'VND/tháng')