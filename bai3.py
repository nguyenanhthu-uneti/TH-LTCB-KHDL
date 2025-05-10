# Viết chương trình nhập vào các số a, b, c sau đó kiểm tra bộ ba số a, b, c vừa nhập
# vào là bộ ba cạnh của tam giác thường, tam giác vuông, tam giác cân, tam giác
# vuông cân, tam giác đều hay không phải là bộ ba cạnh của tam giác.
a = float(input("Nhâp số a :"))
b = float(input("Nhập số b :"))
c = float(input("Nhập số c :"))
if a > 0 and b > 0 and c > 0:
    if a**2 + b **2 == c**2 or a**2 + c**2 == b**2 or b **2 + c ** 2 == a**2 :
        print("Day la tam gia vuong ")
    elif (a**2 + b **2 == c**2 and a == b ) or (a**2 + c**2 == b**2 and a == c) or ( b **2 + c ** 2 == a**2 and b ==c ):
        print("Day la tam giac vuong can ")
    elif (a == b and a != c)  or (a == c and c!=b) or (b == c and b !=a) :
        print("Day la tam giac can ")
    elif a == b == c :
        print("Day la tam giac deu ")
    else:
        print("Day la tam giac binh thuong ")
else :
    print("Ban nhap sai do dai , vui long nhap lai ")