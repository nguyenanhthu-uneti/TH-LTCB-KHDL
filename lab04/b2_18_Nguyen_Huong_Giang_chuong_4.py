# 2. Tính tổng 
# a) S = 1/1 - 1/2 + 1/3 - 1/4 + 1/5 - ...
# b) 1/2 + 1/2x3 + 1/3x4 + 1/4x5 +...
# c) 1/can2 + 1/can3 + 1/can4 + 1/can5 + ...


# a) S = 1/1 - 1/2 + 1/3 - 1/4 + 1/5 - ...
n = int(input("Nhap so nguyen duong n "))
while n <= 0:
    print("Vui long nhap lai ")
S = 0
i = 1
while i <= n:
    if i % 2 == 1:
        S += 1 / i
    else:
        S -= 1 / i
    i += 1
print("Tổng S =", S)
# input: nhap vao so nguyen duong n: 4
# output: Tong S : 0.58333333333333

# b) 1/2 + 1/2x3 + 1/3x4 + 1/4x5 +...
n = int(input("Nhap so nguyen duong n "))
while n <= 0:
    print("Vui long nhap lai ")
s2 = 0 
i = 1
while i <= n :
    s2 = s2 + (1/(i *(i +1)) )
    i = i + 1 
print(s2)

# input : Nhap so nguyen duong n 2
# output: 0.6666666666666666


# c) 1/can2 + 1/can3 + 1/can4 + 1/can5 + ...
import math
n = int(input("Nhap so nguyen duong n "))
while n <= 0:
    print("Vui long nhap lai ")
s3 = 0 
i = 2 
while i <= n : 
    s3 = s3 +  1 / (math.sqrt(i))
    i = i + 1 
print(s3)

# input : Nhap so nguyen duong n 4
# output: 1.7844570503761732