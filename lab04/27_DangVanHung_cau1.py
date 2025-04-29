# Nhập giá trị N
n = int(input("Nhập N: "))
while n <= 0:
    n = int(input("N phải là số nguyên dương. Nhập lại N: "))

#a)
s_4 = 0
i = 0
while i <= n:
    s_4 += i ** 2
    i += 1
print("Tổng S4 là:", s_4)

#b)
s_5 = 0
i = 0
while i < n:
    s_5 += (2 * i + 1) ** 3
    i += 1
print("Tổng S5 là:", s_5)

#c)
s_6 = 0
i = 1
while i <= n:
    s_6 += (2 * i) ** 4
    i += 1
print("Tổng S6 là:", s_6)
