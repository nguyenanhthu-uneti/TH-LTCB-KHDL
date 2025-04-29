while True:
    tu_so = int(input("Nhập tử số: "))
    mau_so = int(input("Nhập mẫu số: "))
    if mau_so != 0:
        break
    print("Mẫu số không được bằng 0. Vui lòng nhập lại.")

print("Phân số bạn nhập là:", tu_so, "/", mau_so)
