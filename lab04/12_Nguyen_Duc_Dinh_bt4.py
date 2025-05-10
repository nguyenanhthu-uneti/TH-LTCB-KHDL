a = float(input("Nhập vào số a: "))
b = float(input("Nhập vào số b: "))
c = float(input("Nhập vào số c: "))
if a > b and a > c:
    print("a là số lớn nhất")
elif a==b and (a > c or b > c):
    print("a và b là 2 số lớn nhất")
elif a == c and (a > b or c > b):
    print("a và c là 2 số lớn nhất")
elif b == c and (b > a or c > a):
    print("b và c là 2 số lớn nhất")
elif b > a and b > c:
    print("b là số lớn nhất")
elif a == b == c:
    print("3 số bằng nhau nên không có số nào lớn nhất")
else:
    print("c là số lớn nhất")
