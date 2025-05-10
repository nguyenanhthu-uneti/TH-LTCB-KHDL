tuso = int(input("Nhập tử số: "))
while True:
    mauso = int(input("Nhập mẫu số: "))
    if mauso != 0:
        break
    print("Mẫu số không được bằng 0. Vui lòng nhập lại.")
print("Phân số:", tuso, "/", mauso)
