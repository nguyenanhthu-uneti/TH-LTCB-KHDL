import math
x =float(input("Nhập giá trị x (radian): "))

epsilon = 1e-4  # Sai số cho phép
cos_x = 1  # Giá trị đầu tiên của chuỗi Taylor
term = 1
n = 0

while abs(term) > epsilon:
    n += 1
    term *= -x**2 / ((2 * n) * (2 * n - 1))
    cos_x += term

print(f"cos({x}) ≈ {cos_x}")
print(f"Giá trị thực tế từ math.cos: {math.cos(x)}")