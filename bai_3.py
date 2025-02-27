a=float(input("Nhap diem a: "))
b=float(input("Nhap diem b: "))
c=float(input("Nhap diem c: "))
if a>0 and b>0 and c>0:
    if a==b==c:
        print("Day la tam giac deu")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("Dau la tam giac vuong")
    elif (a**2+b**2==c**2 and a==b) or (a**2+c**2==b**2 and a==c) or (b**2+c**2==a**2 and b==c):
        print("Day la tam giac vuong can")
    elif a==b or a==c or c==b:
        print("Day la tam giac can")
    else:
        print("Day la tam giac thuong")
else:
    print("Day khong phai la tam giac")
    