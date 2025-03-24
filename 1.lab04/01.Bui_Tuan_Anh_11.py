menu = ["Cafe", "Cam vắt", "Nước ép cà rốt", "Nước lọc", "Nước dừa"]
print("Menu đồ uống:")
i = 0
while i < 5:
    print(i + 1, ".", menu[i])
    i += 1
chon = 0
while chon < 1 or chon > 5:
    chon = int(input("Nhập số để chọn đồ uống: "))
    if chon < 1 or chon > 5:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

print("Bạn đã chọn:", menu[chon - 1])
