n = int(input("Nhập số n: "))
#a)
S_a = 0
i = 1
while i <= n:
    S_a += (-1) ** (i + 1) / i
    i += 1
print("Tổng a:", S_a)
#b) 
S_b = 0
i = 1
while i <= n:
    S_b += 1 / (i * (i + 1))
    i += 1
print("Tổng b:", S_b)
#c) 
import math
S_c = 0
i = 1
while i <= n:
    S_c += 1 / math.sqrt(i + 1)
    i += 1
print("Tổng c:", S_c)