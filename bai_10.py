thang = int(input("Nhập tháng (1-12): "))
nam = int(input("Nhập năm: "))
if thang < 1 or thang > 12:
    print("Tháng không hợp lệ")
else:
    ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if thang == 2:
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            so_ngay = 29 
        else:
            so_ngay = 28 
    else:
        so_ngay = ngay_trong_thang[thang - 1]
    print(f"Số ngày trong tháng {thang} của năm {nam} là: {so_ngay} ngày")
