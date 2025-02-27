a=float(input("Nhap diem a: "))
b=float(input("Nhap diem b: "))
c=float(input("Nhap diem c: "))
if a>b and b>c:
    print("So a la lon nhat")
elif b>a and b>c:
    print("So b la lon nhat")
elif c>a and c>b:
    print("So c la lon nhat")
elif a==b and a>c:
    print('So a va b la lon nhat')
elif a==c and a>b:
    print("So a va c la lon nhat")
elif b==c and b>a:
    print("So b va c la lon nhat")

