# input:Nhap so nguyen duong n: 5
# output:S1 = 0.7833333333333332
        # S2 = 0.8333333333333334
        # S3 = 2.231670645876131
import math  
n = int(input("Nhap so nguyen duong n: "))
Sa=0
Sb=0
Sc=0
while n <= 0:
    n = int(input("Yeu cau nhap lai so nguyen duong n "))

i = 1
while i <= n:
    if i % 2 == 0:
        Sa -= 1 / i
    else:
        Sa += 1 / i
    i += 1
print(f"S1 = {Sa}")
i = 1
while i <= n:
    Sb += 1 / (i * (i + 1))
    i += 1
print(f"S2 = {Sb}")

i = 2
while i <= n:
    Sc += 1 / math.sqrt(i)
    i += 1
print(f"S3 = {Sc}")
