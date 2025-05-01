a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))

x, y = a, b
while y != 0:
    x, y = y, x % y

bcnn = abs(a * b) // x
print(f"Bội chung nhỏ nhất của {a} và {b} là {bcnn}")


# Nhập số nguyên thứ nhất: 4
# Nhập số nguyên thứ hai: 2
# Bội chung nhỏ nhất của 4 và 2 là 4