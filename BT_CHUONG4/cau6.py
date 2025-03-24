n = int(input("Nhập một số: "))
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
ket_qua = ""
while n > 0:
    ket_qua = chu_so[n % 10] + " " + ket_qua
    n //= 10