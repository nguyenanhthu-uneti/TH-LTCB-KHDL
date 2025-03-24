#Viet chuong trinh tim boi chung nho nhat cua hai so nguyen duoc nhap tu ban phim
a = int(input("Nhap vao so thu nhat: "))
b = int(input("Nhap vao so thu hai: "))
x, y = a, b
while b != 0:
    a, b = b, a % b
ước_chung_lớn_nhất = a
bội_chung_nhỏ_nhất = (x * y) // ước_chung_lớn_nhất 
print("Bội chung nhỏ nhất là:", bội_chung_nhỏ_nhất)
# Nhập số thứ nhất: 2
# Nhập số thứ hai: 4
# Bội chung nhỏ nhất là: 4
