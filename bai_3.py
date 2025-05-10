import math
a = int(input("Nhap vao gia tri a "))
b = int(input("Nhap vao gia tri b "))
c = int(input("Nhap vao gia tri c "))
if a + b > c or a + c > b or b + c > a:
    print(" Khong phai la bo ba canh cua tam giac ")
elif a == b == c:
    print(" Day la tam giac deu ")
elif a**2 +  b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 :
        print("Day la tam giac vuong")
elif a**2 + b**2 == c**2:
     print(" Day la tam giac vuong can ")
elif a == b or a == c or b == c:
     print("Day la tam giac can ")
else:
    print("Day la tam giac thuong ")