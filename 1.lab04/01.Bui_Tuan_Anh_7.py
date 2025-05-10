a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
x, y = a, b
while y:
    x, y = y, x % y
bcnn = (a * b) // x
print("Bội chung nhỏ nhất là:", bcnn)
