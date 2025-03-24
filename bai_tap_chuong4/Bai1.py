while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n > 0:
        break
    print("Vui lòng nhập lại")
#a)
S4 = 0
i = 1
while i <= n:
    S4 += i ** 2
    i += 1
print("S4 =", S4)
#b)
S5 = 0
i = 0
while i < n:
    S5 += (2 * i + 1) ** 3
    i += 1
print("S5 =", S5)
#c)
S6 = 0
i = 1
while i <= n:
    S6 += (2 * i) ** 4
    i += 1
print("S6 =", S6)
