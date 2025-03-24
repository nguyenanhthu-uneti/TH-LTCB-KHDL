i = int(input("Nhập vào tử số nguyên dương : "))
while True:
    n = int(input("Nhập vào mẫu số nguyên dương : "))
    if n != 0:
        break
    print("nhập lại")
print(f"{i}/{n}")