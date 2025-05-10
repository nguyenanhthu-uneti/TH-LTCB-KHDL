R = float(input("Nhap gia tri R: "))
x = float(input("Nhap gia tri x: "))
y = float(input("Nhap gia tri y: "))
a = float(input("Nhap gia tri a: "))
b = float(input("Nhap gia tri b: "))
khoang_cach_binh_phuong = (x - a) ** 2 + (y - b) ** 2
duong_kinh = R**2
if khoang_cach_binh_phuong < duong_kinh:
    print("True ,Diem m nam trong hinh tron")
elif khoang_cach_binh_phuong == duong_kinh:
    print("True ,Diem m nam tren hinh tron")
else:
    print("False ,Diem m nam ngoai hinh tron")