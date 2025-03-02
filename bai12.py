LUONG_CO_BAN = 1350000  

def tinh_luong(tnct):
    """Hàm tính lương dựa trên thâm niên công tác"""
    if tnct < 12:
        he_so = 2.34
    elif 12 <= tnct < 36:
        he_so = 3.33
    elif 36 <= tnct < 60:
        he_so = 3.66
    else:  # TNCT >= 60 tháng
        he_so = 3.99
    
    luong = he_so * LUONG_CO_BAN
    return he_so, luong

# Nhập thâm niên công tác từ người dùng
try:
    tnct = int(input("Nhập số tháng làm việc của nhân viên: "))

    if tnct < 0:
        print("Thâm niên công tác không thể là số âm!")
    else:
        he_so, luong = tinh_luong(tnct)
        print(f"Hệ số lương: {he_so}")
        print(f"Lương của nhân viên: {luong} đồng")  # Hiển thị có dấu phẩy phân tách
except :
    print("Vui lòng nhập một số nguyên hợp lệ!")
