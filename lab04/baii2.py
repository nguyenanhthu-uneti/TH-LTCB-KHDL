while True:
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n > 0:
            break
        else:
            print("Vui lòng nhập một số nguyên dương.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")



#a)1/1 - 1/2 + 1/3 - 1/4 + .....
S1 = 0
i = 1
sign = 1
while i <= n:
    S1 += sign * (1/i)
    sign *= -1
    i += 1
print(f"Tổng S1 = {S1}")

# b) S = 1/2 + 1/(2.3) + 1/(3.4) + 1/(4.5) + ...
S2 = 0
i = 2
while i <= n:
    S2 += 1/(i * (i+1))
    i += 1
print(f"Tổng S2 = {S2}")

# c) S = 1/sqrt(2) + 1/sqrt(3) + 1/sqrt(4) + 1/sqrt(5) + ...
import math
S3 = 0
i = 2
while i <= n:
    S3 += 1/math.sqrt(i)
    i += 1
print(f"Tổng S3 = {S3}")


#Nhập số nguyên dương n: 3
# Tổng S1 = 0.8333333333333333
# Tổng S2 = 0.25
# Tổng S3 = 1.2844570503761732