import math
x = float(input("Nhập x (radian): "))
cos_x = 1
so_hang = 1
n = 0
sai_so = 1e-4 
while abs(so_hang) > sai_so:
    n += 1 
    term *= -x**2 / (2 * n * (2 * n - 1)) 
    cos_x += term
print("cos(x) xấp xỉ", cos_x)
print("Giá trị thực của cos(x):", math.cos(x))
