n = int(input("Nhập năm n: "))
if n % 4 == 0 and n % 100 != 0 :
    print("Đây là năm nhuận")
elif n % 400 == 0 :
    print("Đây là năm nhuận")
else :
    print("Đây không phải năm nhuận")
