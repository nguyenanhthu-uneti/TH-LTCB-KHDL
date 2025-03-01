thang = int(input("nhập vào tháng bạn muốn biết:"))
if thang == 1 :
    print("tháng 1 có 31 ngày")
elif thang == 2 :
    nam = int(input("vui lòng nhập năm:"))
    if nam % 4 == 0 and nam % 100 != 0:
        print(f"{nam} là năm nhuận.Tháng 2 có 29 ngày")
    elif nam % 400 == 0:
        print(f"{nam} là năm nhuận.Tháng 2 có 29 ngày")
    else:
        print(f"{nam} là năm không nhuận.Tháng 2 có 28 ngày")
elif thang == 3:
    print(f"tháng {thang} có 31 ngày")
elif thang == 4:
    print(f"tháng {thang} có 30 ngày")
elif thang == 5:
    print(f"tháng {thang} có 31 ngày")
elif thang == 6:
    print(f"tháng {thang} có 30 ngày")
elif thang == 7:
    print(f"tháng {thang} có 31 ngày")
elif thang == 8:
    print(f"tháng {thang} có 31 ngày")
elif thang ==9 :
    print(f"tháng {thang} có 30 ngày")
elif thang == 10 :
    print(f"tháng {thang} có 31 ngày")
elif thang == 11:
    print(f"tháng {thang} có 30 ngày")
elif thang == 12 :
    print(f"tháng {thang} có 31 ngày")
else:
    print("không hợp lệ. vui lòng nhập lại")
