x = int(input("nhap vao toa do x:"))
y = int(input("nhap vao toa do y:"))
a = int(input("nhap vao toa do a:"))
b = int(input("nhap vao toa do b:"))
R = int(input("nhap vao toa do R:"))
n = ((x - a)**2 +(y - b)**2)**(1/2)
print(n)
if n < R**2:
                  print("M nam trong duong tron")
elif n == R**2:
                  print("M nam tren duong tron")
else: 
                  print("M nam ngoai duong tron")
