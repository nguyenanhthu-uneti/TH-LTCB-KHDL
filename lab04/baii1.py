while True:
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n > 0:
            break
        else:
            print("Vui lòng nhập một số nguyên dương.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")


S4 = 0
i = 1
while i <= n:
    S4 += i**2
    i += 1
print(f"Tổng S4 = {S4}")


S5 = 0
i = 1
while i <= n:
    S5 += (2*i - 1)**3
    i += 1
print(f"Tổng S5 = {S5}")


S6 = 0
i = 1
while i <= n:
    S6 += (2*i)**4
    i += 1
print(f"Tổng S6 = {S6}")



# Nhập số nguyên dương n: 4
# Tổng S4 = 30
# Tổng S5 = 496
# Tổng S6 = 5664