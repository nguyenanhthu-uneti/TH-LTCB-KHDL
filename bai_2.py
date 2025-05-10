import math
x = int(input("Nhap vao hoanh do x cua diem M "))
y = int(input("Nhap vao tung do y cua diem M "))
a = int(input("Nhap vao hoanh do a cua tam I "))
b = int(input("Nhap vao tung do b cua tam I "))
R = int(input("Nhap vao ban kinh hinh tron "))
khoang_cach= ((x-a)**2 + (y-b)**2)**(1/2)
print(khoang_cach)
if khoang_cach < R:
    print(" Diem M nam trong hinh tron ")
elif khoang_cach == R:
    print(" Diem M nam tren hinh tron ")
else:
    print("Diem M nam ngoai hinh tron ")