a = float(input("Nhập vào số a: "))
b = float(input("Nhập vào số b: "))
c = float(input("Nhập vào số c: "))
if a > 0 and b > 0 and c > 0:
    if a + b > c or a + c > b or b + c > a:
        print(" Ba cạnh cạnh a,b,c tạp thành 1 tam giác ")
    else:
        if a == b == c:
            print("tam giác đều ")
        elif a**2 + b**2 == c**2 and a**2 + c**2 == b**2 and c**2 + b**2 == a**2 :
            print(" Tam giavs vuông ")
        elif a== b or a== c or b==c :
            print (" Tam giác cân ")
        else:
            print("Tam giác thường ")
else:
    print(" Không phải ba cạnh của tam giác! ")

