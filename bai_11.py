
so = input("Nhập số nguyên có 3 chữ số: ")
if len(so) != 3 or not so.lstrip('-').isdigit():
    print("Vui lòng nhập một số nguyên có đúng 3 chữ số.")
else:
    cach_doc = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    if so[0] == '-':
        ket_qua = "âm " + " ".join(cach_doc[int(digit)] for digit in so[1:])
    else:
        ket_qua = " ".join(cach_doc[int(digit)] for digit in so)
    print(f"Số {so} được đọc là: {ket_qua}")
