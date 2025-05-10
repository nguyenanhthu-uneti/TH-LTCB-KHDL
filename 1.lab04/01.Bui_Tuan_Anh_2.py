while True:
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n > 0:
            break
        print("Vui lòng nhập số nguyên dương.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
S1 = 0
i = 1
while i <= n:
    if i % 2 == 1:
        S1 += 1 / i
    else:
        S1 -= 1 / i
    i += 1
print("S1 =", S1)
S2 = 0
i = 2
while i <= n:
    S2 += 1 / (i * (i + 1))
    i += 1
print("S2 =", S2)
S3 = 0
i = 2
while i <= n:
    S3 += 1 / (i ** 0.5)
    i += 1
print("S3 =", S3)
