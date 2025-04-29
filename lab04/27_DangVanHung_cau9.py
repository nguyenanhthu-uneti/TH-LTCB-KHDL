so = input("Nhập một số: ")
tong = 0
index = 0

while index < len(so):
    chu_so = int(so[index])
    tong += chu_so
    index += 1

print("Tổng các chữ số là:", tong)
