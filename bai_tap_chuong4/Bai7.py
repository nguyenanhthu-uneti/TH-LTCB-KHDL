a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

while a <= 0 or b <= 0:
    a = int(input("Nhập lại a: "))
    b = int(input("Nhập lại b: "))

# Tìm BCNN bằng cách duyệt từ max(a, b)
bcnn = max(a, b)
while bcnn % a != 0 or bcnn % b != 0:
    bcnn += 1

print("BCNN là:", bcnn)