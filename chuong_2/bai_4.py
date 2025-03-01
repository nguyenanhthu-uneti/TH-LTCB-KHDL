a = float(input("Nhập số thứ 1: "))
b = float(input("Nhập số thứ 2: "))
c = float(input("Nhập số thứ 3: "))
if a >= b and a >= c:
    SLN = a
elif b >= a and b >= c:
    SLN = b
else:
    SLN = c
print(f"Vậy số lớn nhất là: {SLN}")