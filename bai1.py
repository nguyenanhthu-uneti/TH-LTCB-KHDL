n = int(input("Nhập số năm vào đây: "))
if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print("Đây là năm nhuận")
else:
    print("Không phải năm nhuận")
