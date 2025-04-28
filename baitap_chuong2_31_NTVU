#bai1
n = int(input("nhập số năm : "))
if n % 4 == 0 and n % 100 != 0 :
    print("là năm nhuận")
elif n % 400 == 0 :
    print("là năm nhuận")
else :
    print("k là nằm nhuận")

#bai2
x = float(input("nhập giá trị x :"))
y = float(input("nhập giá trị y :"))
a = float(input("nhập giá trị a :"))
b = float(input("nhập giá trị b:"))
IM = ((x-a)**2 + (y-b)**2)**(1/2)
r = float(input("nhập giá trị bán kính"))
if IM == r or IM < r:
    print ("TRUE")
else:
    print("FALSE")

#bai3
a = float(input("nhập giá trị cạnh a :"))
b = float(input("nhập giá trị cạnh b :"))
c = float(input("nhập giá trị cạnh c :"))
if a + b <= c or a + c <= b or b + c <= a :
    print("k phải tam giác")
else :
    canh = sorted([a , b ,c ])
    if canh[0]**2 + canh[1]**2 == canh[2]**2:
        print("là tam giác vuông")
    if (a==b) or (a==c) or (b==c) :
        print("là tam giác cân")
    if canh[0]**2 + canh[1]**2 == canh[2]**2 and( (a==b) or (a==c) or (b==c) ) :
        print("là tam giác vuông cân ")
    if a==b==c :
        print("tam giác đều ")

#bai4
#Tìm số lớn nhất trong ba số a, b, c
a = float(input("Nhập số a :"))
b = float(input("Nhập số b :"))
c = float(input("Nhập số c :"))
if a != b and a != c and b !=c:
    if a > b and a > c:
        print("a là số lớn nhất")
    elif b > a and b > c:
        print("b là số lớn nhất")
    else:
        print("c là số lớn nhất")
elif a == b or a == c or b == c:
    if a == b:
        if a > c:
            print(f'{a} la so lon nhat')
        else:
            print(f'{c} la so lon nhat')
    if a == c:
        if a > b:
            print(f'{a} la so lon nhat') 
        else:
            print(f'{b} la so lon nhat')
    if b == c:
        if b > a:
            print(f'{b} la so lon nhat')
        else:
            print(f'{a} la so lon nhat')

#bai5
chu=str(input("Nhập một kí tự bất kì trong bảng chữ cái tiếng anh :"))
ki_tu = "ueoaiUEOAi"
if chu.isalpha() : 
    if chu in ki_tu : 
        print(f'Kí tự {chu} là nguyên âm')
    else:
        print(f'Kí tự {chu} là phụ âm')
else:
    print("lỗi")

#bai6   
print("Nhap lua chon cua ban")
print("1. Phim tinh cam")
print("2. Phim kkinh di")
print("3. Phim hoat hinh")
print("4. Phim khoa hoc vien tuong")
n = int(input("Nhập thứ tự phim bạn muốn xem:"))
if n == 1:
    print("Bạn đã chọn phim tình cảm")
elif n == 2:
    print("Bạn đã chọn phim kinh dị")
elif n == 3:
    print("Bạn đã chọn phim hoạt hình")
elif n == 4:
    print("Bạn đã chọn phim khoa học viễn tưởng")
else:
    print("Hãy chọn lại phim")

#bai8
n = str(input("Nhập điểm của sinh viên :"))
if n == "A":
    print(" Sinh viên loại xuất sắc")
elif n == "B":
    print("Sinh viên loại giỏi")
elif n == "C":
    print("Sinh viên loại khá")
elif n == "D":
    print("Sinh viên loại trung bình")
elif n == "E":
    print("Sinh viên loại yếu")
elif n == "F":
    print("Sinh viên loại kém")
#bai9
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
print("Tiền lương thực nhận là: %0.2f"%luong_rong,'VN/tháng')
#bai10
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
#bai11
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
#bai12
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
