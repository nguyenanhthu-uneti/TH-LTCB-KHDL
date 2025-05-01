def nhap_so():
    while True:
        so = float(input("Nhập một số: "))
        if so < 0:
            print("Bạn đã nhập số âm. Chương trình dừng lại.")
            break

nhap_so()

# Nhập một số: 4
# Nhập một số: 5
# Nhập một số: 6
# Nhập một số: -6
# Bạn đã nhập số âm. Chương trình dừng lại.
