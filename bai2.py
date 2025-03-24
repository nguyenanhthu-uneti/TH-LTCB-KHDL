#Kiểm tra điểm M(x,y) đối với hình tròn tâm I(a,b) bán kính 
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
 