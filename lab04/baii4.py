def nhap_phan_so():
    tu_so = int(input("Nhập tử số: "))
    while True:
        mau_so = int(input("Nhập mẫu số: "))
        if mau_so != 0:
            break
        print("Mẫu số không được bằng 0. Vui lòng nhập lại.")
    
    print(f"Phân số bạn vừa nhập: {tu_so}/{mau_so}")

nhap_phan_so()
# Nhập tử số: 1
# Nhập mẫu số: 3
# Phân số bạn vừa nhập: 1/3
