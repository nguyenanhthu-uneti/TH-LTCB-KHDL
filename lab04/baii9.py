so_nhap = input("Nhập một số nguyên: ")

while not so_nhap.isdigit():  
    so_nhap = input("Vui lòng nhập số hợp lệ: ")

tong = 0
i = 0

while i < len(so_nhap):
    i += 1

print(f"Tổng các chữ số của {so_nhap} là {tong}")


# Vui lòng nhập số hợp lệ: 23
# Tổng các chữ số của 23 là 0