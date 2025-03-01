a = float(input("Nhập vào cạnh a: "))
b = float(input("Nhập vào cạnh b: "))
c = float(input("Nhập vào cạnh c: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
            print("Đây là bộ 3 cạnh của tam giác đều")
    elif (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2) and (a == b or a == c or b == c):
            print("Đây là bộ 3 cạnh của tam giác vuông cân")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Đây là bộ 3 cạnh của tam giác vuông")
    elif a == b or a == c or b == c:
            print("Đây là bộ 3 cạnh của tam giác cân")
    else:
            print("Đây là bộ 3 cạnh của tam giác thường")
else:
    print("Ba cạnh không tạo thành tam giác!")
