# 1. Viết chương trình nhập n là số nguyên dương. Nếu n<=0 thì yêu cầu nhập lại. Sau
# đó tính các tổng sau bằng vòng lặp (while):
# a) S4 = 1**2 + 2**2 + 3**2 + ... + n**2
# b) S5 = 1**3 + 3**3 + 5**3 + ... + (2n+1)**3
# c) S6 = 2**4 + 4**4 + 6**4 + ... + (2n)**4

# a) S4 = 1**2 + 2**2 + 3**2 + ... + n**2

n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    print("Vui lòng nhập lại")
S4 = 0
i = 1
while i <= n:
    S4 += i**2
    i += 1
print("Tổng S4 =", S4)

# input: nhap vao so nguyen duong n: 2
# output: Tong S4 : 5



# b) S5 = 1**3 + 3**3 + 5**3 + ... + (2n+1)**3

n = int(input("Nhập số dương n: "))
while n <= 0:
    n = int(input("Vui lòng nhập lại số nguyên dương n: "))
S5 = 0
i = 0
while i < n:
    so_le = 2 * i + 1  
    S5 += so_le ** 3
    i += 1
print("Tổng S5 =", S5)
# input: nhap vao so nguyen duong n: 5
# output: Tong S5 : 1225

# c) S6 = 2**4 + 4**4 + 6**4 + ... + (2n)**4 

n = int(input("Nhập vào sô n nguyên dương "))
while n <= 0:
    print("Vui lòng nhập lại ")
S6 = 0
i = 2  
while i <= 2 * n:
    S6 += i ** 4
    i += 2 
print("Tổng S6 =", S6)
# input: nhap vao so nguyen duong n: 3
# output: Tong S4 : 1568
