so_don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
so_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi",
           "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
n = int(input("Nhập số nguyên có ba chữ số: "))
if not 100 <= abs(n) <= 999:
    print("Vui lòng nhập số nguyên có đúng ba chữ số.")
else:
    ket_qua = "Âm " if n < 0 else ""
    n = abs(n)
    tram = n // 100
    chuc = (n // 10) % 10
    don_vi = n % 10
    ket_qua += so_don_vi[tram] + " trăm"
    if chuc == 0 and don_vi == 0:
        pass
    elif chuc == 0:
        ket_qua += " linh " + so_don_vi[don_vi]
    else:
        ket_qua += " " + so_chuc[chuc]
        if don_vi != 0:
            if don_vi == 1 and chuc >= 2:
                ket_qua += " mốt"
            elif don_vi == 5 and chuc > 0:
                ket_qua += " lăm"
            else:
                ket_qua += " " + so_don_vi[don_vi]
    print(ket_qua)