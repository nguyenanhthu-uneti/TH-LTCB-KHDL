a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Không phải tam giác")
elif a == b == c:
    print("Tam giác đều")
elif a == b or b == c or a == c:
    print("Tam giác cân" + (" vuông" if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 else ""))
elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Tam giác vuông")
else:
    print("Tam giác thường")
