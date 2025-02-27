x=int(input("Nhap diem x: "))
y=int(input("Nhap diem y: "))
a=int(input("Nhap diem a: "))
b=int(input("Nhap diem b: "))
R=int(input("Nhap ban kinh R: "))
dk=True
m=((x+a)**2+(y-b)**2)**(1/2)
if m>R:
    dk=False
    print(dk)
else:
    dk=True
    print(dk)
