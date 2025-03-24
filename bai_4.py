num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))
num3 = float(input("Nhập số thứ ba: "))
max_num = num1
if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3
print("Số lớn nhất trong ba số là:", max_num)