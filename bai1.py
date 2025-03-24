# input:4
# output:S4 = 30
    #    S5 = 1225
    #    S6 = 5664
n = int(input("Nhap so nguyen duong n: "))
S4=0
S5=0
S6=0
i = 0
while n <= 0:
    n = int(input("Yeu cau nhap lai: "))

i = 1
while i <= n:
    S4 += i**2
    i += 1
print(f"S4 = {S4}")

i = 1
while i <= 2*n + 1:
    S5 += i**3
    i += 2
print(f"S5 = {S5}")

i = 2
while i <= 2*n:
    S6 += i**4
    i += 2
print(f"S6 = {S6}")
    