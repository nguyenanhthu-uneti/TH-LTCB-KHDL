print("Menu đồ uống:")
print('1: Cafe')
print("2: Cam vắt")
print("3: Nước ép cà rốt")
print("4: Nước lọc")
print("5: Nước dừa")
while True:
    try:
        chon = int(input("Chọn một món từ menu (1-5): "))
        if chon == 1:
            print(f"Bạn đã chọn: cafe ")
            break
        elif chon == 2:
            print(f"Bạn đã chọn: cam vắt ")
            break
        elif chon == 3:
            print(f"Bạn đã chọn: nước ép cà rốt ")
            break
        elif chon == 4:
            print(f"Bạn đã chọn: nước lọc ")
            break
        elif chon == 5:
            print(f"Bạn đã chọn: nước dừa ")
            break
        else:
            print("chọn lại từ 1 đến 5.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
