a = float(input("nhap vao a:"))
b = float(input("nhap vao b:"))
c = float(input("nhap vao c:"))
if a >= b and a >= c:
                  so_lon_nhat = a
elif b >= a and b >= c:
                  so_lon_nhat = b
else:
                  so_lon_nhat = c
print(f"so lon nhat trong 3 so la {so_lon_nhat}")
