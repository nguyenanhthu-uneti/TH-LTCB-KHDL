import math   
x = float(input("Nhập tọa độ x của điểm M: "))
y = float(input("Nhập tọa độ y của điểm M: "))
a = float(input("Nhập toa độ a của tâm I: "))
b = float(input("Nhập tọa độ b của tâm I: "))
R = float(input("Nhập bán kính R của hình tròn: "))
d = math.sqrt((x-a) ** 2 * (x-b) ** 2)
if d <= R:
    print(True)
else:
    print(False)
