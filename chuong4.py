# #bai1

# n = int(input("nhap n: "))
# while n <= 0:
#     print("nhap sai nhap lai")
#     n = int(input("Nhap n : "))

# #a
# S4 = 0
# i = 1
# while i <= n:
#     S4 += i**2
#     i += 1
# print("S4 =", S4)
# #b
# S5 = 0
# i = 0
# while i < n:
#     S5 += (2 * i + 1) ** 3
#     i += 1
# print("s5", S5)
# #c
# S6 = 0
# i = 2
# while i <= 2 * n:
#     S6 += i**4
#     i += 2
# print("S6 =", S6) #n=3 ketqua=14,153,1568
# #bai2
# import math
# n = int(input("nhap n: "))
# while n <= 0:
#     print("nhap sai nhap lai")
#     n = int(input("Nhap n : "))
# #a
# Sa = 0
# i = 1
# while i <= n:
#     Sa += (-1)**(i+1) / i
#     i += 1
# print("Sa =", Sa)
# #b
# Sb=0
# i = 1
# while i <= n:
#     Sb += 1 / (i * (i+1))
#     i += 1
# print("Sb =", Sb)
# #c
# Sc = 0
# i = 2
# while i <= n:
#     Sc += 1 / math.sqrt(i)
#     i += 1
# print("Sc =", Sc)
#  #nhap n: 3
# # Sa = 0.8333333333333333
# # Sb = 0.75
# # Sc = 1.2844570503761732
# #bai3
# import math

# x = float(input("Nhập x để tính cos(x): "))

# cos_x = 1
# gia_tri = 1 
# n = 1


# while gia_tri > 1e-4 or gia_tri < -1e-4:  
#     gia_tri *= -x**2 / ((2*n) * (2*n-1)) 
#     cos_x += gia_tri
#     n += 1
# print("cos(x) ≈", cos_x)
# #Nhập x để tính cos(x): 3
# #cos(x) ≈ -0.989994494902419
# #bai4
# tu_so = int(input("nhap tu so: "))

# mau_so = int(input("nha mau so: "))
# while mau_so == 0:
#     print("vui long nhap so lon hon 0.")
#     mau_so = int(input("nhap mau so: "))

# print(f"ket qua: {tu_so}/{mau_so}")
# # nhap tu so: 2
# # nha mau so: 3
# # ket qua: 2/3
# #bai5
# while True:  
#     so = float(input("nhap vao gia tri: "))
#     if so < 0:
#         print("so am.")
#         break  
# # nhap vao gia tri: 4
# # nhap vao gia tri: 324
# # nhap vao gia tri: -5
# # so am.
# # bai6

# chu_so = ["khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]

# so = input("Nhập so: ")


# if so[0] == '-':
#     print("am", end=" ")
#     so = so[1:]  
# i = 0
# while i < len(so):
#     print(chu_so[int(so[i])], end=" ")
#     i += 1 
# print()
# # Nhap so: 12345
# # mot hai ba bon nam 
# #bai7

# a = int(input("nhap so thu nhat: "))
# b = int(input("nhap so thu hai: "))


# x, y = a, b
# while y != 0:
#     x, y = y, x % y  

# ucln = x 
# bcnn = abs(a * b) // ucln 
# print(f"BCNN({a}, {b}) =", bcnn)
# # nhap so thu nhat: 5
# # nhap so thu hai: 3
# # BCNN(5, 3) = 15
# #bai8  

# ky_tu = input("Nhập một ký tự: ")


# while len(ky_tu) != 1:
#     print("Vui lòng nhập chỉ một ký tự!")
#     ky_tu = input("Nhập một ký tự: ")


# ascii_value = ord(ky_tu)


# print(f"Giá trị ASCII của '{ky_tu}' là {ascii_value}")
# # Nhập một ký tự: A
# # Giá trị ASCII của 'A' là 65
# #bai9

# so = input("Nhập một số: ")

# if so[0] == '-':
#     so = so[1:]

# tong = 0
# i = 0
# while i < len(so):
#     tong += int(so[i])
#     i += 1

# # print("Tổng các chữ số là:", tong)
# # # Nhập một số: 12
# # # Tổng các chữ số là: 3
# #bai10
# chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

# so = input("Nhập một số thập phân: ")

# if so[0] == '-':
#     print("âm", end=" ")
#     so = so[1:]  

# if "." in so:
#     phan_nguyen, phan_thap_phan = so.split(".")  # Chia số thành 2 phần
# else:
#     phan_nguyen = so
#     phan_thap_phan = ""

# i = 0
# while i < len(phan_nguyen):
#     print(chu_so[int(phan_nguyen[i])], end=" ")
#     i += 1

# if phan_thap_phan:
#     print("phẩy", end=" ")  
#     j = 0
#     while j < len(phan_thap_phan):
#         print(chu_so[int(phan_thap_phan[j])], end=" ")
#         j += 1

# print()  
# # Nhập một số thập phân: 1.6
# # một phẩy sáu 
# #bai11

# print("Menu đồ uống:")
# print("1. Cafe")
# print("2. Cam vắt")
# print("3. Nước ép cà rốt")
# print("4. nước lọc")
# print("5. nước dừa")

# lua_chon = input("nhap lua chon(1-5) : ")

# while lua_chon not in ["1", "2", "3", "4", "5"]:
#     print("nhap sai")
#     lua_chon = input("Nhập lua chon(1-5) ")

# if lua_chon == "1":
#     print("chon thanh cong cafe")
# elif lua_chon == "2":
#     print("chon thanh cong cam vat")
# elif lua_chon == "3":
#     print("chon thanh cong nuoc ep ca rot")
# elif lua_chon == "4":
#     print("nuoc loc!")
# else:
#     print("nuoc dua")
# # Menu đồ uống:
# # 1. Cafe
# # 2. Cam vắt
# # 3. Nước ép cà rốt
# # 4. nước lọc
# # 5. nước dừa
# # nhap lua chon(1-5) : 5
# # nuoc dua
import math

# Nhập giá trị x từ người dùng
x = float(input("Nhập giá trị x (radian): "))

cos_thuc = math.cos(x)  # Giá trị cos(x) thực sự
epsilon = 1e-4  # Sai số cho phép
n = 2  # Bắt đầu từ n = 2

while True:
    cos_x_approx = 1 - (x**2) / (n * (n - 1))  # Công thức truy hồi
    if abs(cos_x_approx - cos_thuc) < epsilon:  # Kiểm tra sai số
        break
    n += 1  # Tăng n để kiểm tra tiếp

print(f"Giá trị nhỏ nhất của n thỏa mãn điều kiện là: {n}")