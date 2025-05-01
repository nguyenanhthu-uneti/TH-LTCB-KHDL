import math
x = float(input("nhap tọa đọ điểm M: "))
y = float(input("nhap tọa đọ điểm M: "))
a = float(input("nhap tọa đọ điểm a: "))
b = float(input("nhap tọa đọ điểm b: "))
R = float(input("nhap bán kính R: "))
IM = math.sqrt((x-a)**2 + (y-b)**2)
print(f"đoạn IM là:{IM}")
if IM < R:
    print (f"diem M nam trong duong tron")
elif IM == R:
    print(f"diem m nam tren duong tron")
else:
    print(f"diem M nam ngoai duong tron")