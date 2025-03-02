a= float(input("nhap canh a:"))
b= float(input("nhap canh b:"))
c= float(input("nhap canh c:"))
if a == 0 or b == 0 or c == 0:
    print("Khong phai la tam giac")
else:
    if a == b == c:
        print("Day la tam giac deu")
    elif a == b or a == c or b == c:
        print("Day la tam giac can")
    elif a == ((b**2 + c**2)**(1/2)) or b == ((a**2 + c**2)**(1/2)) or c == ((a**2 + b**2)**(1/2)):
        print("Day la tam giac vuong") 
    elif a == ((b**2 + c**2)**(1/2)) or b == ((a**2 + c**2)**(1/2)) or c == ((a**2 + b**2)**(1/2)) and a == b or b == c or a == c:
        print("Day la tam giac vuong can")
    else:
        print("Day la tam giac thuong")