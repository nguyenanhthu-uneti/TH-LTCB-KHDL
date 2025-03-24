import math
n = int(input("nhap so nguyen n : "))
while n <= 0 :
    n = int(input("Nhap lai so nguyen dương n la : "))
s = 0 
dau = 1 
i = 1 
while i <= n :
    s = s + (dau * (1/i))
    dau = -dau 
    i = i + 1 
print(s)
s2 = 0 
i = 1
while i <= n :
    s2 = s2 + (1/(i *(i +1)) )
    i = i + 1 
print(s2)
s3 = 0 
i = 2 
while i <= n : 
    s3 = s3 +  1 / (math.sqrt(i))
    i = i + 1 
print(s3)
#input    nhap so nguyen n : 3
#output    # 0.8333333333333333
            # 0.75
            # 1.2844570503761732