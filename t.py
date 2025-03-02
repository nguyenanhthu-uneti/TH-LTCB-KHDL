# #Bai 1:input:2024
#        output:Day la nam nhuan
a = int(input("Nhap nam:"))
if a % 4 == 0 and a % 100 != 0:
    print("Day la nam nhuan")
elif a % 400 == 0:
    print("Day la nam nhuan")
else:
    print("Khong la nam nhuan")
# 

#Bai 2:
# input x=2,y=1,a=4,b=1,R=5
# output:True
import math
x = int(input("Nhap x:"))
y = int(input("Nhap y:"))
a = int(input("Nhap a:"))
b = int(input("Nhap b:"))
r = int(input("Nhap R:"))
if math.sqrt((x-a)**2+(y-b)**2)<=r:
    print(True)
if math.sqrt((x-a)**2+(y-b)**2)>r:
    print(False)
# 
# 
#Bai 3:
# input:a=4,b=4,c=6
# output:Tam giac can
a = float(input("Nhap a:"))
b = float(input("Nhap b:"))
c = float(input("Nhap c:"))
if a > 0 and b > 0 and c > 0:
    if a**2 == b**2 + c**2 or  a**2 + b**2 == c**2 or b**2 ==a**2+ c**2:
        print("Tam giac vuong")
    elif a==b!=c or a==c!=b or b==c!= a:
        if a**2 == b**2 + c**2 or  a**2 + b**2 == c**2 or b**2 ==a**2+ c**2:
            print("Tam giac vuong can")
        else:
            print("Tam giac can")
    elif a==b==c:
        print("Tam giac deu")
    elif a+b>c or a+c>b or b+c>a :
        print("Tam giac thuong")
    else:
        print("Khong phai bo ba canh cua tam giac")
else:
    print("Khong phai bo ba canh cua tam giac")
# 
# 
#Bai4:
# input a=5,b=5,c=2
# output:5 la so lon nhat
a = float(input("Nhap so dau tien:"))
b = float(input("Nhap so thu hai:"))
c = float(input("Nhap so thu ba:"))
if a>= b and a >= c:
    print(f"{a} la so lon nhat")
elif b >=a and b>=c:
    print(f"{b} la so lon nhat")
elif c>= a and c >=b:
    print(f"{c} la so lon nhat")
    
#Bai5:
# input: m
# output:m la phu am
a = str(input("Nhap ki tu:"))
if a in "u,e,o,a,i,U,O,E,A,I":
    print(f"{a} la nguyen am")
else:
    print(f"{a} la phu am")

#Bai6:
# input:1
# output:Danh sach phim kinh di
print("---MENU---")
print("1.phim kinh di")
print("2.Phim khoa hoa vien tuong")
print("3.phim hai")
print("4.Phim hoat hinh")
print("5.Thoat")
a = int(input("Nhap lua chon:"))
if a == 1:
    print("Danh sach phim kinh di:")
elif a == 2:
    print("Danh sach phim khoa hoc vien tuong")
elif a == 3:
    print("Danh sach phim hai")
elif a == 4:
    print("Danh sach phim hoat hinh")
else:
    print("Lua chon khong ton tai")
    # 

#Bai8:
# input:A
# output:Sinh vien loai xuat sac
a = str(input("Nhap diem:"))
if a == "A":
    print("Sinh vien loai xuat sac")
if a == "B":
    print("Sinh vien loai gioi")
if a == "C":    
    print("Sinh vien loai kha")
if a == "D":
    print("Sinh vien loai trung binh")
if a == "E":
    print("Sinh vien loai yeu")
if a == "F":
    print("Sinh vien loai kem")


#Bai9:
# input:20
# output:Thue la:6.0 Trieu
      #Luong rong la:14.0 Trieu
a = float(input("Nhap luong nhan vien(TrieuVND): "))
if a < 7:
    thue = a * 0.1
    print(f"Thue la:{thue}(TrieuVND)")
    print(f"Luong rong la:{a-thue}(TrieuVND)")
elif a >= 7 and a < 15:
    thue = a * 0.2
    print(f"Thue la:{thue}(TrieuVND)")
    print(f"Luong rong la:{a-thue}(TrieuVND)")
elif a >= 15:
    thue = a * 0.3
    print(f"Thue la:{thue}(TrieuVND)")
    print(f"Luong rong la:{a-thue}(TrieuVND)")
    

# Bai 10:
# input:1
#output:30 ngay
a = int(input("Nhap thang:"))
if a == 1:
    print("31 ngay")
elif a == 2:
    b = int(input("Nhap nam: "))
    if b % 4 == 0 and b % 100 != 0:
        print("29 ngay")
    elif b % 400 == 0:
        print("29 ngay")
    else:
        print("28 ngay")
elif a == 3:
     print("31 ngay")
elif a == 4:
     print("30 ngay")
elif a == 5:
     print("31 ngay")
elif a == 6:
     print("30 ngay")
elif a == 7:
     print("31 ngay")
elif a == 8:
     print("31 ngay")
elif a == 9:
     print("30 ngay")
elif a == 10:
     print("31 ngay")
elif a == 11:
     print("30 ngay")
elif a == 12:
     print("31 ngay") 
#Bai 11:
#input: nhap hang tram: 1
#       nhap hang chuc: 2
#       nhap hang don vi: 3
# output:1 tram 2 muoi 3
tram = int(input("nhap hang tram: "))
chuc = int(input("nhap hang chuc: "))
donvi = int(input("nhap hang don vi: "))
if tram!=0 and chuc!=0 and donvi!=0:
    print(f"{tram} tram {chuc} muoi {donvi}")
elif tram!=0 and chuc==0 and donvi!=0:
    print(f"{tram} tram linh {donvi}")
elif tram!=0 and chuc==0 and donvi==0:
    print(f"{tram} tram ")
elif tram!=0 and chuc==1 and donvi!=0:
    print(f"{tram} tram muoi {donvi}")
elif tram!=0 and chuc==1 and donvi==0:
    print(f"{tram} tram muoi")
elif tram!=0 and chuc!=0 and donvi==0:
    print(f"{tram} tram {chuc} muoi")

elif tram==0 and chuc!=0 and donvi!=0:
    print(f"{chuc} muoi {donvi}")
elif tram!=0 and chuc==0 and donvi!=0:
    print(f"{donvi}")
elif tram==0 and chuc==1 and donvi!=0:
    print(f"muoi {donvi}")
elif tram==0 and chuc==1 and donvi==0:
    print(f"muoi")
elif tram==0 and chuc==0 and donvi==0:
    print(f"khong")
   
#Bai 12:
# input:66
# output:Luong la:5386500.0 dong
a = int(input("Nhap tham nien cong tac: "))
if a < 12:
    luong = 1350000*2.34
    print(f"Luong la:{luong} dong")
if a >= 12 and a < 36:
    luong = 1350000*3.33
    print(f"Luong la:{luong} dong")
if a >= 36 and a < 60:
    luong = 1350000*3.66
    print(f"Luong la:{luong} dong")
if a >= 60:
    luong = 1350000*3.99
    print(f"Luong la:{luong} dong")