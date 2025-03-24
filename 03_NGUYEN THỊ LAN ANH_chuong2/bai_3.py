a = int(input("Nhap vao canh a: "))
b = int(input("Nhap vao canh b: "))
c = int(input("Nhap vao canh c: "))
if a>0 and b>0 and c>0 and (a+b)>c and (b+c)>a and (a+c)>b:
    if a==b==c:
        print("Tam giac deu")
    elif a==b!=c or a==c!=b or b==c!=a:
        print("Tam giac can")
    elif (a==b and (c**2)==(a**2)+(b**2)) or (a==c and (b**2)==(a**2)+(c**2)) or (b==c and (a**2)==(b**2)+(c**2)):
        print("Tam giac vuong can")
    elif (a**2)==(b**2)+(c**2) or (b**2)==(c**2)+(a**2) or (c**2)==(b**2)+(a**2):
        print("Tam giac vuong")
    else:
        print("Tam giac thuong")
else:
    print("Khong phai tam giac")