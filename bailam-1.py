# Bài 1:
nam = int(input("Nhập năm: "))
if nam % 4 == 0 and nam % 100 != 0:
    print("Đây là năm nhuận")
elif nam % 400 == 0:
    print("Đây là năm nhuận")
else:
    print("Đây không phải là năm nhuận")

# |Đầu vào:                  | Đầu ra:
# |Nhập năm: 2024            | Đây là năm nhuận
# |Nhập năm: 2021            | Đây không phải là năm nhuận


####################################################################################
# Bài 2:
import math
x = float(input("Nhập tọa độ x của điểm M: "))
y = float(input("Nhập tọa độ y của điểm M: "))
a = float(input("Nhập tọa độ a của tâm I: "))
b = float(input("Nhập tọa độ b của tâm I: "))
R = float(input("Nhập bán kính R: "))
IM = math.sqrt((x - a) ** 2 + (y - b) ** 2)
print(f" Khoảng cách IM là: {IM}")
if IM <= R:
    print("True")
else:
    print("False")



# |Đầu vào:                          |Đầu ra:
# |Nhập tọa độ x của điểm M: 2       |Nhập bán kính R: 4
# |Nhập tọa độ y của điểm M: 4       |Khoảng cách IM là: 1.0
# |Nhập tọa độ a của tâm I: 2        |True
# |Nhập tọa độ b của tâm I: 3        |
# |Nhập bán kính R: 4                |
#
# |Nhập tọa độ x của điểm M: 2       |Nhập bán kính R: 4
# |Nhập tọa độ y của điểm M: 4       |Khoảng cách IM là: 2.23606797749979
# |Nhập tọa độ a của tâm I: 1        |False
# |Nhập tọa độ b của tâm I: 2        |
# |Nhập bán kính R: 22               |



#####################################################################################
# Bài 3:
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Đây là tam giác đều.")
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Đây là tam giác vuông cân.")
        else:
            print("Đây là tam giác cân.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Đây là tam giác vuông.")
    else:
        print("Đây là tam giác thường.")
else:
    print("Không phải là bộ ba cạnh của tam giác.")


# Đầu vào:
# Nhập cạnh a: 2         |Nhập cạnh a: 2            |Nhập cạnh a: 3         
# Nhập cạnh b: 2         |Nhập cạnh b: 4            |Nhập cạnh b: 4         
# Nhập cạnh c: 2         |Nhập cạnh c: 3            |Nhập cạnh c: 5         
# Đầu ra:
# Đây là tam giác đều.   |Đây là tam giác thường.   |Đây là tam giác vuông. 



################################################################################
# Bài 4:
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
# Giả sử số lớn nhất là a
SLN = a
if b >= a and b >= c:
    SLN = b
elif c >= a and c >= b:
    SLN = c
else:
    SLN = a
print(f"Vậy số lớn nhất là: {SLN}")

# Đầu vào:
# Nhập số thứ nhất: 6
# Nhập số thứ hai: 8
# Nhập số thứ ba: 8
# Đầu ra:
# Vậy số lớn nhất là: 8.0


##################################################################################
# Bài 5:
ky_tu = input("Nhập một ký tự bất kỳ: ")
if ky_tu.isalpha() and ky_tu != "":
    ky_tu = ky_tu.lower()
    if ky_tu in 'euoai':
        print(f"Ký tự '{ky_tu}' là nguyên âm.")
    else:
        print(f"Ký tự '{ky_tu}' là phụ âm.")
else:
    print("Ký tự '{ky_tu}' không phải là nguyên âm hay phụ âm")

# Đầu vào:
# Nhập một ký tự bất kỳ: K     |Nhập một ký tự bất kỳ: o
# Đầu ra:
# Ký tự 'k' là phụ âm.         |Ký tự 'o' là nguyên âm.


##################################################################################################
# Bài 6:
print("Chào mừng bạn đến rạp chiếu phim ABC!")
print("Dưới đây là các thể loại phim hiện đang có:")
print("1. Phim tình cảm")
print("2. Phim kinh dị")
print("3. Phim hoạt hình")
print("4. Phim hành động")
lua_chon = input("Quý khách vui lòng nhập số tương ứng với thể loại phim bạn muốn xem (1-4): ")
if lua_chon == '1':
    print("Bạn đã chọn thể loại: Phim tình cảm.")
elif lua_chon == '2':
    print("Bạn đã chọn thể loại: Phim kinh dị.")
elif lua_chon == '3':
    print("Bạn đã chọn thể loại: Phim hoạt hình.")
elif lua_chon == '4':
    print("Bạn đã chọn thể loại: Phim hành động.")
else:
    print("Lựa chọn không hợp lệ. Quý khách vui lòng nhập lại số từ 1 đến 4.")



# Đầu vào:
# Chào mừng bạn đến rạp chiếu phim ABC!
# Dưới đây là các thể loại phim hiện đang có:
# 1. Phim tình cảm
# 2. Phim kinh dị
# 3. Phim hoạt hình
# 4. Phim hành động
# Quý khách vui lòng nhập số tương ứng với thể loại phim bạn muốn xem (1-4): 3

# Đầu ra:
# Bạn đã chọn thể loại: Phim hoạt hình.


#####################################################################################################
# Bài 8:
diem = input("Nhập điểm (A, B, C, D, E, F): ")

if diem == 'A':
    print("Bạn là sinh viên xuất sắc.")
elif diem == 'B':
    print("Bạn là sinh viên loại giỏi.")
elif diem == 'C':
    print("Bạn là sinh viên loại khá.")
elif diem == 'D':
    print("Bạn là sinh viên loại trung bình.")
elif diem == 'E':
    print("Bạn là sinh viên loại yếu.")
elif diem == 'F':
    print("Bạn là sinh viên xếp loại kém.")
else:
    print("Bạn đã nhập sai rồi. Vui lòng nhập A hoặc B hoặc C hoặc D hoặc E hoặc F.")


# Đầu vào:
# Nhập điểm (A, B, C, D, E, F): B

# Đầu ra:
# Bạn là sinh viên loại giỏi.


###################################################################################################
# Bài 9:
luong = float(input("Nhập lương của nhân viên (đồng): "))
thue = 0
luong_rong = 0
if luong >= 15000000:
    thue = luong * 0.3  
elif luong >= 7000000 and luong < 15000000:
    thue = luong * 0.2
else:
    thue = luong * 0.1
luong_rong = luong - thue
print(f"Lương trước thuế: {luong} đồng")
print(f"Thuế thu nhập: {thue} đồng")
print(f"Lương ròng (lương thực sự nhận): {luong_rong} đồng")

# Đầu vào:
# Nhập lương của nhân viên (đồng): 10000000

# Đầu ra:
# Lương trước thuế: 10000000.0 đồng
# Thuế thu nhập: 2000000.0 đồng
# Lương ròng (lương thực sự nhận): 8000000.0 đồng


##########################################################################################
# Bài 10:
thang = int(input("Nhập vào tháng (1-12): "))
nam = int(input("Nhập vào năm: "))
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    nam_nhuan = True
else:
    nam_nhuan = False

if thang == 2:
    if nam_nhuan:
        so_ngay = 29
    else:
        so_ngay = 28
elif thang in [4, 6, 9, 11]:
    so_ngay = 30
else:
    so_ngay = 31

print(f"Tháng {thang} năm {nam} có {so_ngay} ngày.")


# Đầu vào:
# |Nhập vào tháng (1-12): 2            |Nhập vào tháng (1-12): 2
# |Nhập vào năm: 2024                  |Nhập vào năm: 2021

# Đầu ra:
# |Tháng 2 năm 2024 có 29 ngày.        |Tháng 2 năm 2021 có 28 ngày.


#############################################################################################################
# Bài 11:
so_hang_don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
so_hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
so_hang_tram = ["", "một trăm", "hai trăm", "ba trăm", "bốn trăm", "năm trăm", "sáu trăm", "bảy trăm", "tám trăm", "chín trăm"]

so = int(input("Nhập vào số nguyên có 3 chữ số: "))

tram = so // 100
chuc = (so % 100) // 10
don_vi = so % 10

cach_doc = so_hang_tram[tram]

if chuc == 0 and don_vi != 0:
    cach_doc += " lẻ " + so_hang_don_vi[don_vi]
elif chuc != 0:
    cach_doc += " " + so_hang_chuc[chuc]
    if don_vi != 0:
        cach_doc += " " + so_hang_don_vi[don_vi]
        
print(f"Cách đọc: {cach_doc}")


# Đầu vào:
# Nhập vào số nguyên có 3 chữ số: 345

# Đầu ra:
# Cách đọc: ba trăm bốn mươi năm


############################################################################################################
# Bài 12:
luong_co_ban = 1350000
tnct = int(input("Nhập vào thâm niên công tác (số tháng): "))
if tnct < 12:
    he_so = 2.34
elif 12 <= tnct < 36:
    he_so = 3.33
elif 36 <= tnct < 60:
    he_so = 3.66
else:
    he_so = 3.99

luong = he_so * luong_co_ban
print(f"Lương của nhân viên là: {luong} đồng")

# Đầu vào:
# Nhập vào thâm niên công tác (số tháng): 38
# Đầu ra:
# Lương của nhân viên là: 4941000.0 đồng