import math
x = int(input("nhap hoanh do diem M: "))
y = int(input("nhap tung do diem M: "))
a = int(input("nhap hoanh do tam I: "))
b = int(input("nhap tung do tam I: "))
r = int(input("nhap vao ban kinh R: "))
khoang_cach = math.sqrt((x-a)**2 + (y-b)**2)
print(f"khoang cach la: {khoang_cach:.2f}")
if khoang_cach < r:
    print(True)
else: 
    print(False)
