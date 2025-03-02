a = int(input("nhap so nguyen co 3 chu so: "))
if a < 100 or a > 999:
    print("phai nhap so co 3 chu so:")
else:
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    tram = ["", "một trăm", "hai trăm", "ba trăm", "bốn trăm", "năm trăm", "sáu trăm", "bảy trăm", "tám trăm", "chín trăm"]
    b = a // 100
    c = (a % 100) // 10
    d = a % 10
    ket_qua = tram[b]
    if c == 0 and d == 0:
        print(ket_qua)
    elif c == 0:
        print(ket_qua + " lẻ " + don_vi[d])
    elif c == 1:
        if d == 0:
            print(ket_qua + " mười")
        elif d == 5:
            print(ket_qua + " mười lăm")
        else:
            print(ket_qua + " mười " + don_vi[d])
    else:
        ket_qua += " " + chuc[c]
        if d == 0:
            print(ket_qua)
        elif d == 5:
            print(ket_qua + " lăm")
        else:
            print(ket_qua + " " + don_vi[d])
