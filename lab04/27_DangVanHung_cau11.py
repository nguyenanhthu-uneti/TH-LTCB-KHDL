# Chương trình gọi đồ uống
while True:
    print("\nMenu đồ uống:")
    print("1. Cafe")
    print("2. Cam vắt")
    print("3. Nước ép cà rốt")
    print("0. Thoát")
    c = int(input("Nhập số lựa chọn của bạn: "))

    if c == 1:
        print("Bạn đã chọn Cafe.")
    elif c == 2:
        print("Bạn đã chọn Cam vắt.")
    elif c == 3:
        print("Bạn đã chọn Nước ép cà rốt.")
    elif c == 0:
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
