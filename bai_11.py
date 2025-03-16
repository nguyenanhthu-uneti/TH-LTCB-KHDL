so = int(input("Nhập số nguyên có ba chữ số: "))
if 100 <= so <= 999:
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    tram = ["", "một trăm", "hai trăm", "ba trăm", "bốn trăm", "năm trăm", "sáu trăm", "bảy trăm", "tám trăm", "chín trăm"]
    a = so // 100
    b = (so % 100) // 10
    c = so % 10
    if b == 1 and c == 0:
        cach_doc = f"{tram[a]} mười"
    elif b == 1:
        cach_doc = f"{tram[a]} mười {don_vi[c]}"
    elif b == 0 and c == 0:
        cach_doc = f"{tram[a]}"
    elif b == 0:
        cach_doc = f"{tram[a]} lẻ {don_vi[c]}"
    else:
        cach_doc = f"{tram[a]} {chuc[b]} {don_vi[c]}"
    print(f"Cách đọc số {so} là: {cach_doc}")
else:
    print("Số không phải là số nguyên có ba chữ số.")