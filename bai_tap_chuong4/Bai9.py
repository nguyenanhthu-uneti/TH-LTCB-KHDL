num = input("Nhập một số nguyên: ")
total = 0
i = 0
while i < len(num):
    total += int(num[i])
    i += 1
print("Tổng các chữ số:", total)