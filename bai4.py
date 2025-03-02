a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))

so_lon_nhat = a

if b > so_lon_nhat:
    so_lon_nhat = b

if c > so_lon_nhat:
    so_lon_nhat = c

if a >= b and a >=c and b >= c:
    print(f"Số lớn nhất là {so_lon_nhat}")
