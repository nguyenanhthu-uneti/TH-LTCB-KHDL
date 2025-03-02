a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra điều kiện để ba cạnh tạo thành tam giác
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Tam giác đều")
    else:
        if a == b or b == c or a == c:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                print("Tam giác vuông cân")
            else:
                print("Tam giác cân")
        else:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                print("Tam giác vuông")
            else:
                print("Tam giác thường")
else:
    print("Không phải là tam giác")