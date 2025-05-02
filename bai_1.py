n = int(input("Nhâp năm cần kiểm tra: "))
if n > 0:
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        print(f"Năm {n} là năm nhuận")
    else:
        print("Năm không phải là năm nhuận")
else :
    print("Ban nhập sai năm , vui lòng nhập lại ")