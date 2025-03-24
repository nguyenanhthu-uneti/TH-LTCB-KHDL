#bài 1
n = int(input("nhập năm: "))
if n % 400 == 0:
    print("năm nhuận")
elif n % 100 == 0:
    print("không phải năm nhuận")
elif n % 4 == 0:
    print("năm nhuận")
else:
    print("không phải năm nhuận")
#nhập năm: 2024
#năm nhuận
#bài 2
import math
x = int(input("nhập x: "))
y = int(input("nhập y: "))
a = int(input("nhập a: "))
b = int(input("nhập b: "))
r = int(input("nhập bán kính r: "))
do_dai = math.sqrt(((x - a)**2) - ((y - b)**2))
if do_dai > 0:
    print("False")
elif do_dai <= 0:
    print("True")
else:
    print("True")
#nhập x: 4
#nhập y: 2
#nhập a: 1
#nhập b: 3
#nhập bán kính r: 5
#False
#bài 3
a = int(input("nhập a: "))
b = int(input("nhập b: "))
c = int(input("nhập c: "))
if a + b > c:
    if a == b == c:
        print("abc là tam giác đều")
    elif a == b or b == c:
        if a**2 + b**2 == c**2:
            print("abc là tam giác vuông cân")
        else:
            print("abc là tam giác cân")
    elif a**2 + b**2 == c**2:
        print("abc là tam giác vuông")
    else:
        print("abc là tam giác thường")
else:
    print("abc không phải tam giác")
#nhập a: 2
#nhập b: 6
#nhập c: 2
#abc là tam giác thường
#bài 4
a = int(input("nhập a: "))
b = int(input("nhập b: "))
c = int(input("nhập c: "))
if a >= b or a >= c:
    print("số lớn nhất là: ", a)
elif b >= a or b >= c:
    print("số lớn nhất là: ", b)
else:
    print("số lớn nhất là: ", c)
#nhập a: 2
#nhập b: 2
#nhập c: 1
#số lớn nhất là:  2
#bài 5
ky_tu = input("Nhập một ký tự: ")
if ky_tu in ('u', 'e', 'o', 'a', 'i'):
    print(f"{ky_tu} là nguyên âm.")
else:
    print(f"{ky_tu} là phụ âm.")
#Nhập một ký tự: u
#u là nguyên âm.
#bài 6
print("=====Menu rạp phim ABC=====")
print("chọn thể loại phim")
print("1. kinh dị")
print("2. hài hước")
print("3. hành động")
print("4. hoạt hình")
print("5. tình càm")
lua_chon = input("chọn số tương ứng: ")
if lua_chon == "1":
    print("phim kinh dị")
elif lua_chon == "2":
    print("phim hài hước")
elif lua_chon == "3":
    print("phim hành động")
elif lua_chon == "4":
    print("phim hoạt hình")
elif lua_chon == "5":
    print("phim tình cảm")
else:
    print("lựa chọn không hợp lệ")
#=====Menu rạp phim ABC=====
#chọn thể loại phim
#1. kinh dị
#2. hài hước
#3. hành động
#4. hoạt hình
#5. tình càm
#chọn số tương ứng: 3
#phim hành động
#bài 8
diem = input("Nhập điểm của sinh viên: ")
if diem == 'A':
    print("Sinh viên xuất sắc.")
elif diem == 'B':
    print("Sinh viên giỏi.")
elif diem == 'C':
    print("Sinh viên khá.")
elif diem == 'D':
    print("Sinh viên trung bình.")
elif diem == 'E':
    print("Sinh viên yếu.")
elif diem == 'F':
    print("Sinh viên kém.")
else:
    print("Điểm không hợp lệ!")
#Nhập điểm của sinh viên: E
#Sinh viên yếu.
#bài 9
luong = float(input("Nhập lương nhân viên(triệu): "))
if luong >= 15:
    thue = 0.3
elif 7 <= luong < 15:
    thue = 0.2
else:
    thue = 0.1
thue_thu_nhap = luong * thue
luong_rong = luong - thue_thu_nhap
print("thuế thu nhập là: ",thue_thu_nhap)
print("lương ròng là: ",luong_rong)
#Nhập lương nhân viên(triệu): 11
#thuế thu nhập là:  2.2
#lương ròng là:  8.8
#bài 10
thang = int(input("Nhập tháng: "))
if thang in (1, 3, 5, 7, 8, 10, 12):
    print("Tháng có 31 ngày.")
elif thang in (4, 6, 9, 11):
    print("Tháng có 30 ngày.")
elif thang == 2:
    print("Tháng này có 28 hoặc 29 ngày tùy theo năm nhuận.")
else:
    print("Tháng không hợp lệ!")
#Nhập tháng: 3
#Tháng có 31 ngày.
#bài 11
so = int(input("Nhập số nguyên có ba chữ số: "))
if 100 <= so <= 999:
    hang_tram = so // 100
    hang_chuc = (so // 10) % 10
    hang_dv = so % 10
    doc_so = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    ket_qua = f"{doc_so[hang_tram]} trăm"
    if hang_chuc == 0 and hang_dv != 0:
        ket_qua += f" lẻ {doc_so[hang_dv]}"
    elif hang_chuc == 1:
        if hang_dv == 5:
            ket_qua += " mười lăm"
        elif hang_dv == 0:
            ket_qua += " mười"
        else:
            ket_qua += f" mười {doc_so[hang_dv]}"
    elif hang_chuc > 1:
        ket_qua += f" {doc_so[hang_chuc]} mươi"
        if hang_dv == 5:
            ket_qua += " lăm"
        elif hang_dv != 0:
            ket_qua += f" {doc_so[hang_dv]}"
    print(f"Cách đọc: {ket_qua}")
else:
    print("Số không hợp lệ")
#Nhập số nguyên có ba chữ số: 342
#Cách đọc: ba trăm bốn mươi hai
#bài 12
luong_cb = 1350000
tnct = int(input("thâm niên công tác (tháng): "))
if tnct < 12:
    he_so = 2.34
elif 12 <= tnct < 36:
    he_so = 3.33
elif 36 <= tnct < 60:
    he_so = 3.66
else:
    he_so = 3.99
luong = he_so * luong_cb
print("lương của nhân viên là: ",luong)
#thâm niên công tác (tháng): 24
#lương của nhân viên là:  4495500.0

