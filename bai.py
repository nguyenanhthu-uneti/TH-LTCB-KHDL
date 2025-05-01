#BAI1
n = int(input("Nhap nam n: "))
if n % 4 and n % 100 != 0:
    print("Nam do la nam nhuan")
elif n % 400 :
    print("Nam do la nam nhuan")
#BAI2
import math
a = float(input("nhap gia tri a :"))
b = float(input("nhap gia tri b :"))
x = float(input("nhap gia tri x :"))
y = float(input("nhap gia tri y :"))
r = float(input("nhap gia tri r :"))
kc = math.sqrt((x - a)**2 + (y - b)**2)
print(kc)
if kc > r :
    print("M nam ngoai dg tron")
elif kc == 0:
    print("M nam tren dg tron")
else:
    print("M nam trong dg tron")



#BAI3 
a = float(input("Nhap gia tri a:"))    
b = float(input("Nhap gia tri b:"))    
c = float(input("Nhap gia tri c:"))    
if a > 0 and b > 0 and c > 0:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 :
        print("do la tam giac vuong")
    elif a==b!=c or a==c!=b or b==c!=a:
        print("do la tam giac can")
    elif (a**2 + b**2 == c**2 and a==b!=c) or (a**2 + c**2 == b**2 and a==c!=b) or (b**2 + c**2 == a**2 and b==c!=a):
        print("do la tam giac vuong can")
    elif a == b ==c :
        print("do la tam giac deu")
    else:
        print("do la tam giac thuong")   
else:
    print("3 canh ko thuoc 1 tam giac") 

#BAI4 
a = float(input("nhap gia tri a :"))
b = float(input("nhap gia tri b :"))
c = float(input("nhap gia tri c :"))
if a > b and b > c:
    print("a la so lon nhat")
elif b > a and b > c:
    print("b la so lon nhat")
elif a==b and c<a:
    print("a va b la 2 so lon nhat")
elif a==c and b<a:
    print("a va c la 2 so lon nhat")
elif b == c and a < b:
    print("b va c la 2 so lon nhat")
else:
    print(" c la so lon nhat")
    
    
    
#BAI5
ki_tu = input("NHap 1 ki tu bat ki").lower()
ds_nguyen_am = 'ueoai'
if ki_tu in ds_nguyen_am:
    print("Nguyen am")
else:
    print("Phu am")
    
#BAI6 
while True:
    print("MENU")
    print("1.PHIM A")
    print("2.PHIM B")
    print("3.PHIM C")
    print("4.THOAT")
    chon = float(input("lua chon(1-4):"))
    if chon == 1:
        print("ban chon PHIM A")
    elif chon == 2:
        print("ban chon PHIM B")
    elif chon == 3:
        print("ban chon PHIM C")
    else:
        print("THOAT")
        break
        
    
#BAI8
n = input("Nhap diem(A-F):").upper()
if n == 'A':
    print("hs xuat sac")
elif n == 'B':
    print("hs gioi")
elif n == 'C':
    print("hs kha")
elif n == 'D':
    print("hs trung binh")
elif n == 'E':
    print("hs yeu")    
else:
    print("hs kem")
    

#BAI9
luong = float(input("Nhap so luong:"))
luong_rong = 0
thue = 0
if luong < 7000000:
    thue = luong*0.1
elif luong < 15000000:
    thue = luong*0.2
else:
    thue = luong*0.3
luong_rong = luong - thue
print(f"Thue thu nhap: {thue:.2f} trieu ")
print(f"luong rong thu nhap: {luong_rong:.2f} trieu ")

#BAI10
month = int(input("Nhap thang:"))
if month < 1 and month > 12:
    print("Nhap sai")
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("Thang do co 31 ngay")
elif month == 2: 
    n = int(input("Nhap nam n: "))
    if n % 4 and n % 100 != 0:
        print("Thang 2 co 29 ngay")
    elif n % 400 :
        print("Thang 2 co 29 ngay")
    else:
        print("Thang 2 co 28 ngay")
else:
    print("thang do co 31 ngay")


#BAI12
TNCT = int(input("Nhap cong tac tham nien:"))
luong_co_ban=1350000
if TNCT < 12 :
    he_so = 2.34
elif 36 >= TNCT and TNCT >= 12  :
    he_so = 3.33
elif TNCT >= 36 and TNCT < 60:
    he_so = 3.66
else:
    he_so = 3.99   
luong = luong_co_ban*he_so
print(f"luong:{luong:.2f}")



#BAI 11
def read_number(n):
    ones = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    tens = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    hundreds = ["", "một trăm", "hai trăm", "ba trăm", "bốn trăm", "năm trăm", "sáu trăm", "bảy trăm", "tám trăm", "chín trăm"]
    
    if n < 100 or n > 999:
        return "Số nhập vào không hợp lệ."
    
    h = n // 100
    t = (n // 10) % 10
    o = n % 10
    
    result = hundreds[h]
    
    if t == 0:
        if o != 0:
            result += " linh " + ones[o]
    elif t == 1:
        if o == 0:
            result += " mười"
        elif o == 5:
            result += " mười lăm"
        else:
            result += " mười " + ones[o]
    else:
        result += " " + tens[t]
        if o == 1:
            result += " mốt"
        elif o == 5:
            result += " lăm"
        elif o != 0:
            result += " " + ones[o]
    
    return result

num = int(input("Nhập vào một số nguyên có ba chữ số: "))
print(read_number(num))
