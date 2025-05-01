chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

so = int(input("Nhập số nguyên có ba chữ số: "))

if 100 <= so <= 999:
    tram = so // 100
    chuc = (so // 10) % 10
    don_vi = so % 10

    doc_so = f"{chu_so[tram]} trăm"
    
    if chuc == 0 and don_vi != 0:
        doc_so += " lẻ"
    elif chuc == 1:
        doc_so += " mười"
    elif chuc > 1:
        doc_so += f" {chu_so[chuc]} mươi"

    if don_vi != 0:
        if chuc > 1 and don_vi == 1:
            doc_so += " mốt"
        elif chuc > 0 and don_vi == 5:
            doc_so += " lăm"
        else:
            doc_so += f" {chu_so[don_vi]}"

    
    print(f"Số {so} đọc là: {doc_so}")

else:
    print("Vui lòng nhập số có ba chữ số (100-999).")