import math
while True:
    n = int(input("Nhập vào số nguyên dương n: "))
    if n > 0:
        break
    print("nhập lại")
S1=0
i = 0
while i <= n:
    S1 = S1 + (-1)**i/(i+1)
    i=i+1
   
print(f"Tổng S1 = {S1}")
S2 = 0
i = 1
while i <= n:
    S2 += 1 / (i * (i + 1))
    i += 1
print(f"Tổng S2 = {S2}")

S3 = 0
i = 2
while i <= n:
    S3 += 1 / math.sqrt(i)
    i += 1
print(f"Tổng S3 = {S3}")

