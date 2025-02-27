# Viết chương trình kiểm tra xem điểm M(x, y) có nằm trong hình tròn tâm I(a, b) và bán
# kính R bằng cách xuất ra giá trị True nếu điểm M nằm trong hoặc trên hình tròn và
# False nếu nằm ngoài hình tròn với x, y, a, b, R nhập vào từ bàn phím.
x = float(input("Nhap diem x: "))
y = float(input("Nhap diem y: "))
a = float(input("Nhap diem a: "))
b = float(input("Nhap diem b: "))
ban_kinh_R = float(input("nhap ban kinh R can kiem tra: "))
d = ((x - a)**2 + (y - b)**2)**1/2
if d < ban_kinh_R or d == ban_kinh_R:
    print("True")
    print(f'{d}')
else:
    print("False")
    print(f'{d}')