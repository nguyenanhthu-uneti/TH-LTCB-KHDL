num = int(input("Nhập một số nguyên dương: "))

while num <= 0:
    num = int(input("Nhập lại số nguyên dương: "))

binary = ""
while num > 0:
    binary = str(num % 2) + binary
    num //= 2

print("Số nhị phân:", binary)
