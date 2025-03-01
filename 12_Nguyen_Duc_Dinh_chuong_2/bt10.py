month = int(input("Nhập vào một tháng trong năm (1-12): "))
while month < 1 or month > 12:
    print("Nhập lại tháng hợp lệ")
    month = int(input("Nhập vào một tháng trong năm (1-12): "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("Tháng này có 31 ngày.")
elif month == 2:
    n = int(input("Nhập năm: "))
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        print("Tháng 2 này có 29 ngày.")
    else:
        print("Tháng 2 này có 28 ngày.")
else:
    print("Tháng này có 30 ngày.")
