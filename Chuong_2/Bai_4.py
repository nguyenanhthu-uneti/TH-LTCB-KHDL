num1 = float(input("Nhap gia tri num1: "))
num2 = float(input("Nhap gia tri num2: "))
num3 = float(input("Nhap gia tri num3: "))
max_num = num1
if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3
print("So lon nhat trong 3 so la:", max_num)