#Viet chuong trinh nhap vao mot so nguyen co ba chu so. Hay in ra cach doc cua so nguyen nay
a = int(input("Nhap vao so hang tram: "))
b = int(input("Nhap so hang chuc: "))
c = int(input("Nhap so hang don vi: "))
if a != 0 and b != 0 and c != 0:
    print(f'{a} tram {b} muoi {c}')
elif a != 0 and b == 0 and c != 0:
    print(f'{a} tram linh {c}')
elif a != 0 and b != 0 and c == 0:
    print(f'{a} tram {b} muoi')
elif a != 0 and b == 0 and c == 0:
    print(f'{a} tram')
    