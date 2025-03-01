import math
x = float(input("Nhập tọa độ x của điểm M: "))
y = float(input("Nhập tọa độ y của điểm M: "))
a = float(input("Nhập tọa độ a của tâm I: "))
b = float(input("Nhập tọa độ b của tâm I: "))
R = float(input("NHập bán kính R: "))
d = math.sqrt((x-a)**2 + (y-b)**2)
print('d=',d)
if d <= R:
    print("True")
else:
    print("Fale")