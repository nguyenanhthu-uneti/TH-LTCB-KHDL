import math
x = int(input("Nhap vao x: "))
y = int(input("Nhap vao y: "))
a = int(input("Nhap vao a: "))
b = int(input("nhap vao b: "))
R = int(input("Nhap vao R: "))
IM = math.sqrt(((x-a)**2) + ((y-b)**2))
if IM<R:
    print(f"Diem M({x},{y}) nam trong hinh tron")
elif IM==R:
    print(f"Diem M({x},{y}) nam tren hinh tron")
else:
    print(f"Diem M({x},{y} nam ngoai hinh tron)")