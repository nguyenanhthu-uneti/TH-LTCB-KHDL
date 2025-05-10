a = float(input("Nhap gia tri a: "))
b = float(input("Nhap gia tri b: "))
c = float(input("Nhap gia tri c: "))
if ( a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Tam giac deu")
    elif a == b or a == c or b == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Tam giac vuong can")
        else:
            print("Tam giac can")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Tam giac vuong")
    else:
        print("Tam giac thuong")
else:
    print("Khong phai tam giac")