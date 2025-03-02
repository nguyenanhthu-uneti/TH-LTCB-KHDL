def la_nam_nhuan(nam):
    """Hàm kiểm tra năm nhuận"""
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

def so_ngay_trong_thang(thang, nam):
    """Hàm trả về số ngày trong tháng, có xét năm nhuận"""
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        return 29 if la_nam_nhuan(nam) else 28
    else:
        return None
try:
    thang = int(input("Nhập tháng (1-12): "))
    nam = int(input("Nhập năm: "))

    so_ngay = so_ngay_trong_thang(thang, nam)

    if so_ngay:
        print(f"Tháng {thang} năm {nam} có {so_ngay} ngày.")
    else:
        print("Tháng không hợp lệ! Vui lòng nhập từ 1 đến 12.")
except :
    print("Vui lòng nhập số nguyên hợp lệ cho tháng và năm!")