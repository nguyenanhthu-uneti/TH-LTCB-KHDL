def doc_so_ba_chu_so(n):
    chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    
    tram = n // 100
    chuc = (n % 100) // 10
    don_vi = n % 10
    
    ket_qua = f"{chu_so[tram]} trăm"
    
    if chuc == 0:
        if don_vi != 0:
            ket_qua += f" linh {chu_so[don_vi]}"
    elif chuc == 1:
        if don_vi == 0:
            ket_qua += " mười"
        elif don_vi == 5:
            ket_qua += " mười lăm"
        else:
            ket_qua += f" mười {chu_so[don_vi]}"
    else:
        ket_qua += f" {chu_so[chuc]} mươi"
        if don_vi == 1:
            ket_qua += " mốt"
        elif don_vi == 5:
            ket_qua += " lăm"
        elif don_vi != 0:
            ket_qua += f" {chu_so[don_vi]}"
    
    return ket_qua

n = int(input("Nhập số nguyên có ba chữ số: "))
if 100 <= n <= 999:
    print(doc_so_ba_chu_so(n))
else:
    print("Vui lòng nhập số nguyên có ba chữ số!")