#Bài 1:
n = int(input("Nhập số nguyên dương n:"))
if n % 4 == 0 or n % 100 != 0:
   print("Đây là năm nhuận")
elif n % 400 == 0:
    print("Đây là năm nhuận")
else:
    print("Đây không phải năm nhuận")

#Bài 2:
import math
x = float(input("Nhập x:"))
y = float(input("Nhập y:"))
a = float(input("Nhập a:"))
b = float(input("Nhập b:"))
R = float(input("Nhập R:"))
if math.sqrt((x - a)**2 + (y - b)**2) == R:
    print("True")
elif math.sqrt((x - a)**2 + (y - b)**2) < R:
    print("True")
else:
    print("False")
    
#Bài 3:
import math
a = float(input("Nhập a:"))
b = float(input("Nhập b:"))
c = float(input("Nhập c:"))
if a > 0 and b > 0 and c > 0:
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print("Đây là tam giác vuông")
    elif a == b != c or b == c != a or c == a != b:
        if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
            print("Đây là tam giác vuông cân")
        else:
            print("Đây là tam giác cân")
    elif a == b == c:
        print("Đây là tam giác đều")
    elif a + b == c or a + c == b or b + c == a:
        print("Đây là tam giác thường")
else:
    print("Đây không phải là tamn giác")

#Bài 4:
a = float(input("Nhập a:"))
b = float(input("Nhập b:"))
c = float(input("Nhập c:"))
if a >= b and b >= c and a >= c:
    print(f"{a} là số lớn nhất")
elif b >= a and a >= c and b >= c:
    print(f"{b} là số lớn nhất")
else:
    print(f"{c} là số lớn nhất")

#Bài 5:
a = str(input("Nhập kí tự:"))
if a in "e, u,i,o,a":
    print("Đây là nguyên âm")
else:
    print("Đây là phụ âm")

#Bài 6:
print("a.MENU")
print("1.Phim viễn tưởng")
print("2.Phim hành động")
print("3.Phim khinh dị")
print("4.Phim tình cảm")
print("5.Phim hoạt hình")
a = int(input("Nhập thể loại phim:"))
if a == 1:
    print("1.Phim viễn tưởng")   
elif a == 2:
    print("2.Phim hành động")
elif a == 3:
    print("3.Phim kinh dị")
elif a == 4:
    print("4.Phim tình cảm")
else:
    print("5.Phim hoạt hình")

#Bài 8:
a = input("Nhập loại điểm:")
if a == "A":
    print("Học sinh xuất sắc")
elif a == "B":
    print("Học sinh loại giỏi")
elif a == "C":
    print("Học sinh loại khá")
elif a == "D":
    print("Học sinh trung bình")
elif a == "E":
    print("Học sinh loại yếu")
else:
    print("Học sinh loại kém")

#Bài 9:
a = float(input("NHập thuế thu nhập và lương ròng(VNĐ):"))
if a == 15:
    thuế = a * 0.3
    lương_ròng = a - thuế
    print(f"Thuế là{thuế:.2f}(VNĐ)")
    print(f"Lương ròng là{lương_ròng:2f}(VNĐ)")
elif a >= 7 and a <=15:
    thuế = a * 0.2
    lương_ròng = a - thuế
    print(f"Thuế là{thuế:.2f}(VNĐ)")
    print(f"Lương ròng là{lương_ròng:2f}(VNĐ)")
elif a >= 15:
    thuế = a * 0.1
    lương_ròng = a - thuế
    print(f"Thuế là{thuế:.2f}(VNĐ)")
    print(f"Lương ròng là{lương_ròng:2f}(VNĐ)")

#Bài 10:
a = int(input("Nhập tháng:"))
if a == 1:
    print("Tháng có 31 ngày")
elif a == 2:
    b = int(input("Nhập năm:"))
    if b % 4 == 0 or b % 100 != 0:
        print("Tháng có 28 ngày")
    elif b % 400 == 0:
        print("Tháng có 28 ngày")
    else:
        print("Tháng có 299 ngày")
elif a == 3:
    print("Tháng có 31 ngày")
elif a == 4:
    print("Tháng có 30 ngày")
elif a == 5:
    print("Tháng có 31 ngày")
elif a == 6:
    print("Tháng có 30 ngày")
elif a == 7:
    print("Tháng có 31 ngày")
elif a == 8:
    print("Tháng có 31 ngày")
elif a == 9:
    print("Tháng có 30 ngày")
elif a == 10:
    print("Tháng có 31 ngày")
elif a == 11:
    print("Tháng có 30 ngày")
elif a == 12:
    print("Tháng có 31 ngày")

#Bài 11:
s = int(input("Nhập vào một số nguyên có ba chữ số: "))
if 100 <= s <= 999:
    ones = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    tens = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    
    t = s // 100  
    c = (s // 10) % 10  
    dv = s % 10  

    doc = f"{ones[t]} trăm"
    
    if c != 0:
        if c == 1:
            doc += " mười"
        else:
            doc += f" {tens[c]}"
    
    if dv != 0:
        if c == 1:
            doc += f" {ones[dv]}"
        elif c > 1 or c == 0:
            doc += f" {ones[dv]}"

    print("Số bạn nhập là:", doc)
else:
    print("Vui lòng nhập lại")

#Bài 12:
a = float(input("Nhập thâm niên công tác:"))
if a < 12:
    luong = 2.23 * 1350000
    print(f"luong nhan vien la:{luong}")
elif a >= 12 and a < 36:
    luong = 3.33 * 1350000
    print(f"luong nhan vien la:{luong}")
elif a >= 36 and a < 60:
    luong = 3.66 * 1350000
    print(f"luong nhan vien la:{luong}")
elif a > 60:
    luong = 3.99 * 1350000
    print(f"luong nhan vien la:{luong}")


