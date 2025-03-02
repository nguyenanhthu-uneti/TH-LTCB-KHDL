so = int(input("Nhập một số nguyên có ba chữ số: "))

if 100 <= so <= 999:
    hang_tram = ["", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
    hang_chuc = ["", "Mười", "Hai mươi", "Ba mươi", "Bốn mươi", "Năm mươi", "Sáu mươi", "Bảy mươi", "Tám mươi", "Chín mươi"]
    hang_don_vi = ["", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
    
    tram = so // 100
    chuc = (so % 100) // 10
    don_vi = so % 10
    
    ket_qua = hang_tram[tram] + " trăm"
    
    if chuc == 0 and don_vi == 0:
        print(ket_qua)
    elif chuc == 0:
        print(ket_qua + " lẻ " + hang_don_vi[don_vi])
    elif chuc == 1:
        if don_vi == 0:
            print(ket_qua + " mười")
        else:
            print(ket_qua + " mười " + hang_don_vi[don_vi])
    else:
        if don_vi == 0:
            print(ket_qua + " " + hang_chuc[chuc])
        else:
            if don_vi == 5:
                print(ket_qua + " " + hang_chuc[chuc] + " lăm")
            else:
                print(ket_qua + " " + hang_chuc[chuc] + " " + hang_don_vi[don_vi])
else:
    print("Vui lòng nhập một số nguyên có ba chữ số.")
