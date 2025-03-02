# Nhập ba số
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
if a >= b and a >= c:
    resurt = a
elif b >= a and b >= c:
    resurt = b
else:
    resurt = c
print("Số lớn nhất trong ba số là:", resurt)
