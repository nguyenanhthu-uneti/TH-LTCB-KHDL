# Tính năm nhuận. Năm thứ n là nhuận nếu có chia hết cho 4, nhưng không chia hết
# cho 100 hoặc năm đó chia hết cho 400 (Chú ý: một số nguyên a là chia hết cho b
# nếu phần dư của phép chia bằng 0, tức a % b == 0)
n = int(input("Nhâp năm cần kiểm tra: "))
if n > 0:
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        print(f"Năm {n} là năm nhuận")
    else:
        print("Năm không phải là năm nhuận")
else :
    print("Ban nhập sai năm , vui lòng nhập lại ")