tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))

while mau_so == 0:
    mau_so = int(input("Mẫu số không thể là 0, nhập lại: "))

print(f"Phân số: {tu_so}/{mau_so}")