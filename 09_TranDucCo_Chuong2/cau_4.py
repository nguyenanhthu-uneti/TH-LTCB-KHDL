# Viết chương trình tìm số lớn nhất trong 3 số bằng Python.
a = float(input("Nhập số a :"))
b = float(input("Nhập số b :"))
c = float(input("Nhập số c :"))
if a != b and a != c and b !=c: 
    if a > b and a > c:
        print(f"{a} là số lớn nhất")
    elif b > a and b > c:
        print(f"{b} là số lớn nhất")
    else:
        print(f"{c} là số lớn nhất")        
elif a == b or a == c or b == c:
    if a == b:
        if a > c:
            print(f'{a} la so lon nhat')
        else:
            print(f'{c} la so lon nhat')
    if a == c:
        if a > b:
            print(f'{a} la so lon nhat') 
        else:
            print(f'{b} la so lon nhat')
    if b == c:
        if b > a:
            print(f'{b} la so lon nhat') 
        else:
            print(f'{a} la so lon nhat')