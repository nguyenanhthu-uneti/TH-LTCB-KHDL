chu_so = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
while True: 
    n = int(input("Nhap chu so can doc la : "))
    if  100 <= n <= 999 :
        break
    else :
        print("ban nhap ko dung , hay nhap lai ")
if n < 0 : 
    ket_qua = "âm"
    n = abs(n)
else :
    ket_qua = " "
hang_tram = n // 100 
hang_chuc = (n // 10) % 10 
hang_don_vi = n % 10 
ket_qua += chu_so[hang_tram] + " trăm"
if hang_chuc == 0 and hang_don_vi != 0 :
    ket_qua += " lẻ " + chu_so[hang_don_vi]
elif hang_chuc == 1:
    ket_qua += " mười"
    if hang_don_vi != 0:
        ket_qua += " " + chu_so[hang_don_vi]
elif hang_chuc > 1:
    ket_qua += " " + chu_so[hang_chuc] + " mươi"
    if hang_don_vi == 1:
        ket_qua += " mốt"
    elif hang_don_vi == 5:
        ket_qua += " lăm"
    elif hang_don_vi != 0:
        ket_qua += " " + chu_so[hang_don_vi]
print("Cách đọc:", ket_qua)