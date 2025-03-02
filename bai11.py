def doc_so(n):
    tram = ["", "Một trăm", "Hai trăm", "Ba trăm", "Bốn trăm", "Năm trăm", "Sáu trăm", "Bảy trăm", "Tám trăm", "Chín trăm"]
    chuc = ["", "Mười", "Hai mươi", "Ba mươi", "Bốn mươi", "Năm mươi", "Sáu mươi", "Bảy mươi", "Tám mươi", "Chín mươi"]
    dv = ["", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]

    t, c, d = n // 100, (n // 10) % 10, n % 10
    return f"{tram[t]} {'linh' if c == 0 and d else chuc[c]} {('mốt' if d == 1 and c > 1 else 'lăm' if d == 5 and c > 0 else dv[d]) if d else ''}".strip()

n = int(input("Nhập số có ba chữ số: "))
print(doc_so(n))