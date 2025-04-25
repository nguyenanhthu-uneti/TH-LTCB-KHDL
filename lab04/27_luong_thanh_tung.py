#Bài 1
#a,
n=int(input("Nhap: "))
a=0
b=1
while b<=n:
    a=a+b**2
    b=b+1
print(a)
# n=5
#kq=55

#b,
n=int(input("Nhap: "))
a=1
b=1
while b<=n:
    a=a+(2*b+1)**3
    b=b+1
print(a)
# n=4
# kq=1225

#c,
n=int(input("Nhap: "))
a=0
b=1
while b<=n:
    a=a+(2*b)**4
    b=b+1
print(a)
#n=3
#kq=1536

#Bài 2
#a,
n=int(input("Nhap: "))
a=0
b=0
while b<n:
    a=a+((-1)**b/(b+1))
    b=b+1
print(a)
#n=4
#kq=0.583333333

#b,
n=int(input("Nhap: "))
a=0
b=1
while b<=n:
    a=a+(1/(b*(b+1)))
    b=b+1
print(a)
#n=5
#kq=0.8333333333333334
#c,
n=int(input("Nhap: "))
a=0
b=2
while b<=n:
    a=a+(1/b**(1/2))
    b=b+1
print(a)
#n=3
#kq=1.2844570503761732

#Bài 3
import math

x=int(input('Nhap x: '))
if x <= 1:
    print('Nhap x > 1')
else:
    kq=0
    n=1
    while abs(kq - ((x ** 3) / ((n+1) * ((n+1) - 1)))) <= 0.0001:
        kq=1 +(((-1) ** n) * (x ** (2 * n))) / math.factorial(2 * n)
        n=n+1
        
    print(f"So {n} va {x} thoa man dk")
       
#Bài 4
a=float(input("Nhap so tu: "))
while True:
    b=float(input("Nhap so mau: "))
    if b!=0:
        break
    else:
        print("Nhap so mau khac 0")
print(f"Phan so: {a:.0f}/{b:.0f}")
#a=4
#b=3
#kq=4/3
       
#Bài 5
while True:
    n=float(input("Nhap a: "))
    if n<=0:
        print("Nhap a > 0")
    else:   
        print(f"So n = {n}")
        break
#n=-4
#kq=Nhap a > 0

#Bài 6
n = int(input("Nhập một số: "))
chu_so = {0: "không", 1: "một", 2: "hai", 3: "ba", 4: "bốn", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín"}
ket_qua = ""

if n < 0:
    print("Vui lòng nhập một số không âm.")
else:
    while n > 0:
        ket_qua = chu_so[n % 10] + " " + ket_qua
        n //= 10
    print("Kết quả:", ket_qua.strip())
#n=312
#kq: ba một hai

#Bài 7
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
x, y = a, b
while b != 0:
    a, b = b, a % b
uoc_chung_lon_nhat = a
boi_chung_nho_nhat = (x * y) // uoc_chung_lon_nhat 
print("Bội chung nhỏ nhất là:", boi_chung_nho_nhat)
# a=12, b=18
# ucln=6
# bcnn=36

#Bài 8
ki_tu = ""
while ki_tu == "":
    ki_tu = input("Nhập một ký tự của bạn: ")
ma_ascii = ord(ki_tu)
print("Mã ASCII của", ki_tu, "là:", ma_ascii)
#ki_tu = "a"
#kq=97

#Bài 9
n= int(input("Nhập một số: "))
tong = 0
while n > 0:
    tong += n % 10 
    n //= 10 
print("Tổng các chữ số là:", tong)
#n=123
#kq=6

#Bài 10
so = input("Nhập một số thập phân: ")
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
ket_qua = ""
i = 0 
while i < len(so):
    if so[i] != ".":
        ket_qua += chu_so[int(so[i])] + " "
    i += 1  
print("Kết quả:", ket_qua.strip())
#n=123.45
#kq: một hai ba bốn năm

#Bài 11
print("Menu ")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt")
print("4. Nước lọc")
print("5. Nước dừa")
while True: 
    lua_chon = float(input("Nhập lựa chọn của quý khách:  "))
    if lua_chon == 1 :
        print("Bạn đã oder  Cafe thành công ")
    elif lua_chon == 2 :
        print("Bạn đã oder  Cam vắt thành công")
    elif lua_chon == 3 :
        print("Bạn đã oder  Nước ép cà rốt thành công")
    elif lua_chon == 4 :
        print("Bạn đã oder  Nước lọc thành công")
    elif lua_chon == 5 :
        print("Bạn đã oder  Nước dừa thành công")
    else  :
        print("Bạn nhập quá lựa chọn vui lòng nhập lại nè")
        break
#lua_chon=3
#kq=Bạn đã oder  Nước ép cà rốt thành công