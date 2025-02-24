#bai_1
def is_leap_year(year):  
    """Kiểm tra xem năm có phải là năm nhuận hay không."""  
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  
        return True  
    else:  
        return False  

nhap_nam = int(input("Nhập năm cần kiểm tra: "))  
if is_leap_year(nhap_nam):  
    print(f"Năm {nhap_nam} là năm nhuận.")  
else:  
    print(f"Năm {nhap_nam} không phải là năm nhuận.")

#bai_2
Nhập dữ liệu từ bàn phím  
x = float(input("Nhập giá trị x của điểm M: "))  
y = float(input("Nhập giá trị y của điểm M: "))  
a = float(input("Nhập tọa độ a (x tâm hình tròn): "))  
b = float(input("Nhập tọa độ b (y tâm hình tròn): "))  
R = float(input("Nhập bán kính R của hình tròn: "))  

# Tính khoảng cách từ điểm M đến tâm hình tròn  
khoang_cach = ((x - a) ** 2 + (y - b) ** 2) ** 0.5  

# Kiểm tra xem điểm M có nằm trong hoặc trên hình tròn hay không  
if khoang_cach <= R:  
    print(True)  
else:  
    print(False)

#bai_3
Nhập dữ liệu từ người dùng  
a = float(input("Nhập cạnh a: "))  
b = float(input("Nhập cạnh b: "))  
c = float(input("Nhập cạnh c: "))  

# Sắp xếp các cạnh để dễ dàng kiểm tra  
a, b, c = sorted([a, b, c])  

# Kiểm tra điều kiện tam giác  
if a + b <= c:  
    print("Không phải là bộ ba cạnh của tam giác")
else:
    # Kiểm tra loại tam giác  
    if a == b == c:  
        print("Tam giác đều")  
    elif a == b or b == c or a == c:  
        if a * a + b * b == c * c:  
            print("Tam giác vuông cân")  
        else:  
            print("Tam giác cân")  
    elif a * a + b * b == c * c:  
        print("Tam giác vuông")  
    else:  
        print("Tam giác thường")

#bai_4
so_1 = float(input("Nhập số thứ nhất: "))  
so_2 = float(input("Nhập số thứ hai: "))  
so_3 = float(input("Nhập số thứ ba: "))  

if so_1 >= so_2 and so_1 >= so_3:  
    so_lon_nhat = so_1  
elif so_2 >= so_1 and so_2 >= so_3:  
    so_lon_nhat = so_2  
else:  
    so_lon_nhat = so_3  

print("Số lớn nhất trong 3 số là:", so_lon_nhat)

#bai_5
char = input("Nhập một ký tự: ")  
if len(char) == 1:   
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':  
        if char in 'aeiouAEIOU':  
            print(f"Ký tự '{char}' là nguyên âm.")  
        else:  
            print(f"Ký tự '{char}' là phụ âm.")  
    else:  
        print("Ký tự bạn nhập không phải là chữ cái.")  
else:  
    print("Vui lòng nhập một ký tự hợp lệ (chỉ một chữ cái).")

#bai_6
print("rạp chiếu phim ABC!")  
while True:  
    print("\nDanh sách phim đang chiếu:")  
    print("1. Phim loliloli")  
    print("2. Phim meme")  
    print("3. Phim gầy")    
    print("4. Thoát")  
    lua_chon = input("Vui lòng nhập số phim bạn muốn xem (1-6): ")  
    if lua_chon == '1':  
        print("Bạn đã chọn phim loliloli.")  
    elif lua_chon == '2':  
        print("Bạn đã chọn phim meme.")  
    elif lua_chon == '3':  
        print("Bạn đã chọn phim gầy.")  
    elif lua_chon == '4':  
        print("Bạn đã chọn phim Xếp Hình.")  

#bai_8
Nhập điểm của sinh viên  
diem = float(input("Nhập điểm của sinh viên: "))  

# Phân loại sinh viên dựa vào điểm  
if diem >= 8.5:  
    dt = "Xuất sắc"  
elif diem >= 7.0:  
    dt = "Giỏi"  
elif diem >= 5.5:  
    dt = "Khá"  
elif diem >= 4.0:  
    dt = "Trung bình"  
else:  
    dt = "Yếu"  

# Hiển thị kết quả  
print(f"Điểm: {diem}, Phân loại: {dt}")

#bai_9
# Nhập lương cơ bản và phụ cấp  
luong_co_ban = float(input("Nhập lương cơ bản của nhân viên (VNĐ): "))  
phu_cap = float(input("Nhập các phụ cấp khác (VNĐ): "))  
# Tính tổng lương  
luong_thuc_nhan = luong_co_ban + phu_cap  
# Tính thuế  
if luong_thuc_nhan > 15000000:  
    thue = luong_thuc_nhan * 0.30 
elif luong_thuc_nhan >= 7000000:  
    thue = luong_thuc_nhan * 0.20  
else:  
    thue = luong_thuc_nhan * 0.10

luong_sau_thue = luong_thuc_nhan - thue  
# Hiển thị kết quả  
print(f"\nTổng lương (bao gồm phụ cấp): {luong_thuc_nhan:,.0f} VNĐ")  
print(f"Thuế thu nhập cá nhân: {thue:,.0f} VNĐ")  
print(f"Lương sau thuế: {luong_sau_thue:,.0f} VNĐ")

#bai_10
Nhập vào tháng và năm  
thang = int(input("Nhập tháng (1-12): "))  
nam = int(input("Nhập năm: "))  

# Kiểm tra số ngày trong tháng  
if thang in [1, 3, 5, 7, 8, 10, 12]:  
    so_ngay = 31  
elif thang in [4, 6, 9, 11]:  
    so_ngay = 30  
elif thang == 2:  
    # Kiểm tra năm nhuận  
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):  
        so_ngay = 29  
    else:  
        so_ngay = 28  
else:  
    so_ngay = None  

# In kết quả  
if so_ngay is not None:  
    print(f"Tháng {thang} năm {nam} có {so_ngay} ngày.")  
else:  
    print("Tháng bạn nhập không hợp lệ!")

#bai_11
Nhập số nguyên có 3 chữ số  
num = int(input("Vui lòng nhập một số nguyên có 3 chữ số: "))  

if num < 100 or num > 999:  
    print("Vui lòng nhập một số nguyên có 3 chữ số.")  
else:  
    donvi = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]  
    tram = num // 100  
    chuc = (num // 10) % 10  
    unit = num % 10  

    ket_qua = ""  

    # Cách đọc số trăm  
    if tram > 0:  
        ket_qua += donvi[tram] + " trăm "  
    
    # Cách đọc số chục  
    if chuc > 0:  
        if chuc == 1:  
            ket_qua += "mười "  
        else:  
            ket_qua += donvi[chuc] + " mươi "  
    
    # Cách đọc số đơn vị  
    if unit > 0:  
        if chuc == 0:  
            ket_qua += donvi[unit]  
        else:  
            ket_qua += donvi[unit]  

    print("Cách đọc của số này là:", ket_qua.strip())


#bai_12
luong_co_ban = 1350000  

# Nhập số tháng làm việc  
tnc = int(input("Nhập số tháng làm việc của nhân viên: "))  

# Tính hệ số H dựa trên số tháng làm việc  
if tnc < 12:  
    h = 0.24  
elif 12 <= tnc < 36:  
    h = 0.33  
elif 36 <= tnc < 60:  
    h = 0.50  
else:  
    h = 0.69  

# Tính lương  
luong = h * luong_co_ban  

# In kết quả  
print(f"Lương của nhân viên là: {luong:.2f} đồng")
