a = int(input("Nhap so t1: "))
b = int(input("Nhap so t2: "))
c = int(input("Nhap so t3: "))
if a>=b and a>=c:
    print(f"{a} la so lon nhat trong 3 so")
elif b>=a and b>=c:
    print(f"{b} la so lon nhat trong 3 so")
else:
    print(f"{c} la so lon nhat trong 3 so")