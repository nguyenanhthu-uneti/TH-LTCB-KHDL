#bài 1:
print("chuong trinh kiem tra mot nam co phai nam nhuan khong")
nam= int(input("nhap nam can kiem tra la: "))
if (nam %4==0 and nam%100 !=0) or (nam %400 == 0) :
    print("nam" ,nam, "la nam nhuan!")
else:
    print("nam",nam, "khong phai la nam nhuan !")

#bài 2:
a,b = map(float,input('Nhap toa do tam I: ').split())
r = float(input('nhap ban kinh R: '))
x,y = map(float,input('nhap toa do diem M: ').split())
import math
d = math.sqrt((x-a)**2 + (y+b)**2)
if d<r:
    print('diem M nam trong duong tron')
elif d==r:
    print('diem M nam tren duong tron')
else:
    print('diem M nam ngoai duong tron')
#bài 3:
a,b,c=map(float,input('Nhập độ dài các cạnh: ').split(","))
if a+b<c or b+c<a or c+a<b:
    print('khong phai la do dai 3 canh cua tam giac ')
elif a==b or a==c or b==c:
    if a==b==c:
        print('Đây là tam giác đều')
    elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
        print('Đây là tam giác vuông cân')
    else:
        print('Đây la tam giác cân')
elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
    print('Đây là tam giác vuông')
else:
    print('Đây là tam giác thường')

#bài 4:
print("Nhập các số :",end='')
a,b,c = map(float,input('=').split(','))
max=a
if max < b:
    max = b
if max < c:
    max = c
print('Số lớn nhất trong 3 số %0.2f , %0.2f, %0.2f '%(a,b,c),'là%0.2f'%max)

#bài 5:
print('Nhập ký tự :',end='')
ky_tu=input()
if ky_tu =='O' or ky_tu=='o' or\
   ky_tu =='U' or ky_tu=='u' or\
   ky_tu =='I' or ky_tu=='i' or\
   ky_tu =='A' or ky_tu=='a' or\
   ky_tu =='E' or ky_tu=='e' :
    print("Ký tự '", ky_tu, "' là nguyên âm!")
else:
    print("Ký tự'", ky_tu, "' là phụ âm!")

#bài 6:
print('\n\n\t\t=========MENU======')
print("1. Phim tinh cam")
print("2. Phim kinh di")
print("3. Phim hoat hinh")
print("4. Phim khoa hoc vien tuong")
print('\n\t\t========END=======')
print('Nhap lua chon cua ban (1-->4):',end='')
luachon=int(input())
if luachon==1:
    print('ban da chọn phim tinh cam\n')
elif luachon==2:
    print('ban da chon phim kinh di\n')
elif luachon==3:
    print('ban da chon phim hoat hinh\n')
elif luachon==4:
    print('ban da lua chon the loai phim khoa hoc vien tuong\n')
else:
    print('lua chọn khong hop le vui long kiem tra lai')
   

#bài 8:
print('Chương trình phân loại sinh viên ')
print('Nhập điểm sinh viên,',end='')
loai=input("diem:")
if loai=='A':
    print("Xếp loại xuất sắc")
elif loai=='B':
    print("Xếp loại giỏi")
elif loai=='C':
    print("Xếp loại khá")
elif loai=='D':
    print("Xếp loại trung bình")
elif loai=='E':
    print("Xếp loại yếu")
elif loai=='F':
    print("Xếp loại kém")
else:
    print("Nhập sai vui nhập lại điểm")

#bài 9:
print("Chương trình tính thu nhập (lương ròng) của nhân viên")
luong = float(input("Nhập lương của nhân viên: "))
if luong <=7000000:
    thue_suat=10
    tien_thue=luong*0.1
elif luong <=15000000:
    thue_suat=20
    tien_thue=luong*0.2
else:
    thue_suat=30
    tien_thue=luong*0.3
luong_rong = luong - tien_thue
print("Lương nhân viên: %0.2f"%luong, 'VNĐ/tháng')
print("Thuế suất là %d"%thue_suat,"%")
print("Tiền lương thực nhận là: %0.2f"%luong_rong,'VNĐ/tháng')

#bài 10:
thang= int(input('nhap vao mot thang(1-12): '))
if thang==1 or thang==3 or thang==5 or thang==7 or thang==8 or thang==10 or thang==12:
    print("thang",thang,"co 31 ngay")
if thang==4 or thang==6 or thang==9 or thang==11:
    print("thang",thang,"co 30 ngay")
if thang==2:
    print("chuong trinh kiem tra nam co phai nam nhuan khong")
    nam=int(input("nhap nam can kiem tra: "))
    if (nam %4==0 and nam%100 !=0) or (nam%400==0):
        print("thang",thang,"co 29 ngay")
    else:
        print("thang",thang,"co 28 ngay")

#bai 11:
so=int(input("nhap vao so nguyen co ba chu so:"))
chu_so=("khong","mot","hai","ba","bon","nam","sau","bay","tam","chin")
tram=so//100
chuc=(so//10)%10
don_vi=so%10
if 100<=so<=999:
    print(chu_so[tram],"tram",end=" ")
    if chuc==0 and don_vi==0:
        print()
    elif chuc==0:
        print("le",chu_so[don_vi])
    elif chuc==1:
        if don_vi==0:
            print("muoi")
        elif don_vi==5:
            print("muoi lam")
        else:
            print("muoi",chu_so[don_vi])
    else:
        if don_vi==0:
            print(chu_so[chuc],"muoi")
        elif don_vi==1:
            print(chu_so[chuc],"muoi mot")
        elif don_vi==5:
            print(chu_so[chuc],"muoi lam")
        else:
            print(chu_so[chuc],"muoi",chu_so[don_vi])
else:
    print("so khong hop le")

#bai 12:
tnct=int(input("nhap so thang cong tac: "))
if tnct < 12 :
    he_so = 2.24
elif tnct < 60 :
    he_so = 3.66
else:
    he_so = 3.99
luong_co_ban = 1350000
luong= he_so * luong_co_ban
print(f"luong cua nhan vien : {luong:.0f} dong")
        

        

        





