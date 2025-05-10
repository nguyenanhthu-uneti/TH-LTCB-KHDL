a = int(input("Nhập hàng trăm : "))
b = int(input("Nhập hàng chục  : "))
c = int(input("Nhập hàng đơn vị : "))
if a != 0 or b !=0 or c !=0:
    print(f"{a} trăm {b} mươi {c}")
elif a != 0 or b == 0 or c !=0:
    print(f"{a} trăm linh {c}")
elif a != 0 or b != 0 or c ==0:
    print(f"{a} trăm {b} mươi")
elif a !=0 or b == 0 or c == 0:
    print(f"{a} trăm")
