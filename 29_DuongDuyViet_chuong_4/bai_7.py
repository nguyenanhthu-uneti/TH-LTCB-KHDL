# Nhập vào số nguyên dương a
while True:
    a1 = int(input("Nhập vào số nguyên dương a: "))
    if a1 > 0:
        break
    print("Vui lòng nhập lại số nguyên dương a.")

# Nhập vào số nguyên dương b
while True:
    b1 = int(input("Nhập vào số nguyên dương b: "))
    if b1 > 0:
        break
    print("Vui lòng nhập lại số nguyên dương b.")

# Tính UCLN của a và b bằng thuật toán Euclid
a,b=a1,b1

while b != 0:
    a, b = b, a % b  # Hoán đổi giá trị a, b và tính phần dư

# a hiện tại là UCLN của a và b
ucln = a

# Tính BCNN dựa vào công thức BCNN = (a * b) // UCLN
bcnn = (a1 * b1) // ucln

# In kết quả
print(f"Ước chung lớn nhất của a và b là: {ucln}")
print(f"Bội chung nhỏ nhất của a và b là: {bcnn}")
