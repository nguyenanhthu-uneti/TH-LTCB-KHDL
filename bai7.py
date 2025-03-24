# input:Nhap so nguyen thu nhat: 3
      # Nhap so nguyen thu hai: 4
# output:Boi chung nho nhat cua 3 va 4 la 12 
import math
a = int(input("Nhap so nguyen thu nhat: "))
b = int(input("Nhap so nguyen thu hai: "))

bcnn = abs(a * b) // math.gcd(a, b)

print(f"Boi chung nho nhat cua {a} va {b} la {bcnn}")
