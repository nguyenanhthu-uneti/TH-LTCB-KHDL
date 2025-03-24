a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
x, y = a, b
while b != 0:
    a, b = b, a % b
ước_chung_lớn_nhất = a
bội_chung_nhỏ_nhất = (x * y) // ước_chung_lớn_nhất 
print("Bội chung nhỏ nhất là:", bội_chung_nhỏ_nhất)