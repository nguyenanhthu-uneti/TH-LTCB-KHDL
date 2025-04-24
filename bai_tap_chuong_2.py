#Bai 1
year = int(input("Nhập năm: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} là năm nhuận.")
else:
    print(f"{year} không phải là năm nhuận.")
#Kết quả
#Nhập năm: 2025
#2025 không phải là năm nhuận.



#Bai 2
# Nhập tọa độ điểm M và tâm I cùng bán kính R
x = float(input("Nhập hoành độ x của điểm M: "))
y = float(input("Nhập tung độ y của điểm M: "))
a = float(input("Nhập hoành độ x của tâm I: "))
b = float(input("Nhập tung độ y của tâm I: "))
R = float(input("Nhập bán kính R: "))

# Tính khoảng cách giữa điểm M và tâm I
distance_squared = (x - a) ** 2 + (y - b) ** 2
R_squared = R ** 2

# Kiểm tra điểm M có nằm trong hình tròn không
if distance_squared <= R_squared:
    print(True)  # Điểm M nằm trong hoặc trên hình tròn
else:
    print(False)  # Điểm M nằm ngoài hình tròn
# Kết quả
#Nhập hoành độ x của điểm M: 1
#Nhập tung độ y của điểm M: 2
#Nhập hoành độ x của tâm I: 3
#Nhập tung độ y của tâm I: 4
#Nhập bán kính R: 3
#True

#Bai 3
# Nhập vào ba cạnh a, b, c
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra xem có phải là tam giác không
if a + b > c and a + c > b and b + c > a:
    print("a, b, c là bộ ba cạnh của một tam giác.")
    
    # Kiểm tra loại tam giác
    if a == b == c:
        print("Đây là tam giác đều.")
    else:
        if a == b or a == c or b == c:
            print("Đây là tam giác cân.")
        else:
            if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
                print("Đây là tam giác vuông.")
            else:
                print("Đây là tam giác thường.")
else:
    print("a, b, c không phải là bộ ba cạnh của tam giác.")
# Kết quả
#Nhập cạnh a: 4
#Nhập cạnh b: 5
#Nhập cạnh c: 6
#a, b, c là bộ ba cạnh của một tam giác.
#Đây là tam giác thường.


#Bai 4
# Nhập 3 số từ bàn phím
num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))
num3 = float(input("Nhập số thứ ba: "))

# Tìm số lớn nhất bằng hàm max
max_num = max(num1, num2, num3)

# In ra số lớn nhất
print(f"Số lớn nhất trong ba số là: {max_num}")
# Kết quả
#Nhập số thứ nhất: 3
#Nhập số thứ hai: 2
#Nhập số thứ ba: 7
#Số lớn nhất trong ba số là: 7.0

#Bai 5
char = input("Nhập một ký tự: ").lower()

# Kiểm tra xem ký tự có phải là chữ cái không
if char.isalpha() and len(char) == 1:
    if char in "aeiou":
        print(f"{char} là nguyên âm.")
    else:
        print(f"{char} là phụ âm.")
else:
    print("Ký tự không hợp lệ. Vui lòng nhập một ký tự từ a-z hoặc A-Z.")
# Kết quả
#Nhập một ký tự: j
#j là phụ âm.


#Bai 6
# Hiện menu lựa chọn thể loại phim
print("Chọn thể loại phim bạn muốn xem:")
print("1. Phim tình cảm")
print("2. Phim kinh dị")
print("3. Phim hoạt hình")
print("4. Phim khoa học viễn tưởng")

# Nhập lựa chọn từ người dùng
choice = input("Nhập số tương ứng với thể loại phim: ")

if choice == '1':
    print("Bạn đã chọn Phim tình cảm.")
else:
    if choice == '2':
        print("Bạn đã chọn Phim kinh dị.")
    else:
        if choice == '3':
            print("Bạn đã chọn Phim hoạt hình.")
        else:
            if choice == '4':
                print("Bạn đã chọn Phim khoa học viễn tưởng.")
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 4.")
#Kết quả
#Chọn thể loại phim bạn muốn xem:
#1. Phim tình cảm
#2. Phim kinh dị
#3. Phim hoạt hình
#4. Phim khoa học viễn tưởng
#Nhập số tương ứng với thể loại phim: 3
#Bạn đã chọn Phim hoạt hình.


#Bai 8
a = input("Nhập điểm cho sinh viên: ")
if a == "A":
    xeploai = "Xuất sắc"
elif a == "B":
    xeploai = "Giỏi"
elif a == "C":
    xeploai = "Khá"
elif a == "D":
    xeploai = "Trung bình"
elif a == "E":
    xeploai = "Yếu"
elif a == "F":
    xeploai = "Kém"
else:
    xeploai = "Điểm không hợp lệ"
print(f"Điểm", a ,":", xeploai)
# Kết quả
#Nhập điểm cho sinh viên: 9.0
#Điểm 9.0 : Điểm không hợp lệ


#Bai 9
# Nhập lương nhân viên
luong = float(input("Nhập lương nhân viên (VNĐ): "))

# Tính thuế thu nhập
if luong >= 15000000:
    thue = luong * 0.30
elif luong >= 7000000:
    thue = luong * 0.20
else:
    thue = luong * 0.10

# Tính lương ròng
luong_rong = luong - thue

# Hiển thị kết quả
print(f"Thuế thu nhập: {thue:,.0f} VNĐ")
print(f"Lương ròng: {luong_rong:,.0f} VNĐ")
#Kết quả
#Nhập lương nhân viên (VNĐ): 7000000
#Thuế thu nhập: 1,400,000 VNĐ
#Lương ròng: 5,600,000 VNĐ


#Bai 10
# Nhập tháng
thang = int(input("Nhập tháng (1-12): "))

# Kiểm tra số ngày trong tháng
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    ngay = 31
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    ngay = 30
elif thang == 2:
    # Nhập năm để kiểm tra năm nhuận
    nam = int(input("Nhập năm: "))
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):  # Kiểm tra năm nhuận
        ngay = 29
    else:
        ngay = 28
else:
    ngay = "Tháng không hợp lệ"  # Nếu nhập tháng không hợp lệ

# In kết quả
if isinstance(ngay, int):
    print(f"Tháng {thang} có {ngay} ngày.")
else:
    print(ngay)
#Kết quả
#Nhập tháng (1-12): 10
#Tháng 10 có 31 ngày.


#Bai 11
# Nhập vào số nguyên có 3 chữ số
so = int(input("Nhập vào một số nguyên có ba chữ số: "))

# Kiểm tra số có 3 chữ số hay không
if 100 <= so <= 999:
    # Danh sách các chữ số
    chu_so = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    don_vi = chu_so[so % 10]  # Lấy chữ số đơn vị
    chuc = chu_so[(so // 10) % 10]  # Lấy chữ số chục
    tram = chu_so[(so // 100) % 10]  # Lấy chữ số trăm
    
    # Xử lý các trường hợp đặc biệt (chữ số 5 trong chục)
    if chuc == "năm":
        chuc = "lăm"
    
    # In ra cách đọc số
    if chuc == "":  # Không có chữ số chục (10-19)
        print(f"{tram} trăm {don_vi}")
    elif don_vi == "":  # Không có chữ số đơn vị
        print(f"{tram} trăm {chuc} mươi")
    else:
        print(f"{tram} trăm {chuc} mươi {don_vi}")
else:
    print("Số nhập vào không phải là số nguyên có ba chữ số.")
#Kết quả
#Nhập vào một số nguyên có ba chữ số: 867
#tám trăm sáu mươi bảy

#Bai 12
# Lương cơ bản
luong_co_ban = 1350000

# Nhập thâm niên công tác (TNCT)
tnct = int(input("Nhập thâm niên công tác (tháng): "))

# Xác định hệ số lương dựa trên thâm niên công tác
if tnct < 12:
    he_so = 2.34
elif 12 <= tnct < 36:
    he_so = 3.33
elif 36 <= tnct < 60:
    he_so = 3.66
else:
    he_so = 3.99

# Tính lương
luong = he_so * luong_co_ban

# In kết quả
print(f"Lương của nhân viên là: {luong:,.0f} đồng.")
# Kết quả
#Nhập thâm niên công tác (tháng): 3
#Lương của nhân viên là: 3,159,000 đồng