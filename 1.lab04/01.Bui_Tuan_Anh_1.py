while True:
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n > 0:
            break
        print("Vui lòng nhập số nguyên dương.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
S4 = 0
i = 1
while i <= n:
    S4 += i ** 2
    i += 1
print("S4 =", S4)
S5 = 0
i = 1
while i <= n:
    S5 += (2 * i - 1) ** 3
    i += 1
print("S5 =", S5)
S6 = 0
i = 1
while i <= n:
    S6 += (2 * i) ** 4
    i += 1
print("S6 =", S6)
