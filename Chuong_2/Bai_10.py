so = int(input("Nhap so nguyen có 3 chu so: "))
chu_so = ["khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]
if so < 100 or so > 999:
    print("So khong hop le")
else:
    tram = so // 100
    chuc = (so % 100) // 10
    don_vi = so % 10
    print(f"{so} doc la {chu_so[tram]} tram {chu_so[chuc]} muoi {chu_so[don_vi]}")
