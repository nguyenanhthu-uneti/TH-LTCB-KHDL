n = int(input("Nhập năm :"))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print("Năm", n, "là năm nhuận")
else:
    print("Năm", n, "không phải là năm nhuận")