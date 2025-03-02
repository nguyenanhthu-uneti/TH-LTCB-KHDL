import math
x = float(input("Nhập x: "))
y = float(input("Nhập y: "))
a = float(input("Nhập a: "))
b = float(input("nhap b: "))
R = float(input("nhap ban kinh r: "))
khoang_cach = math.sqrt((x - a) ** 2 + (y - b) ** 2)
print(khoang_cach <= R)