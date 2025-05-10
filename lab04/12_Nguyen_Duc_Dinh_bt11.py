so = int(input("Nhập vào một số nguyên có ba chữ số: "))
if so < 100 or so > 999:
    print("Số nhập vào không phải là số nguyên có ba chữ số.")
else:
    chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    tram = so // 100
    chuc = (so % 100) // 10
    don_vi = so % 10
    doc_so = f"{chu_so[tram]} trăm"
    if chuc == 0:
        if don_vi != 0:
            doc_so += f" linh {chu_so[don_vi]}"
    else:
        if chuc == 1:
            doc_so += f" mười {chu_so[don_vi]}" if don_vi != 0 else " mười"
        else:
            doc_so += f" {chu_so[chuc]} mươi"
            if don_vi != 0:
                if don_vi == 1:
                    doc_so += " mốt"
                elif don_vi == 5:
                    doc_so += " lăm"
                else:
                    doc_so += f" {chu_so[don_vi]}"
    print(doc_so)