# Bài1 
# n = int(input("Nhập số nguyên dương n: "))
# while n <= 0:
#     print("Vui lòng nhập số nguyên dương lớn hơn 0.")
#     n = int(input("Nhập số nguyên dương n: "))
# S4 = 0
# i = 1
# while i <= n:
#     S4 += i**2
#     i += 1
# print(f"S4 = {S4}")

# S5 = 00
# i = 1
# while i <= (2 * n + 1):
#     S5 += i**3
#     i += 2  
# print(f"S5 = {S5}")

# S6 = 0
# i = 2
# while i <= (2 * n):
#     S6 += i**4
#     i += 2  

# print(f"S6 = {S6}")

# Nhập số nguyên dương n:2
# S4 = 2
# S5 = 153
# S6 = 272





# Bài 2
# import math
# n = int(input("Nhập số nguyên dương n: "))
# while n <= 0:
#     print("Vui lòng nhập số nguyên dương lớn hơn 0.")
#     n = int(input("Nhập số nguyên dương n: "))
# S_a = 0
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         S_a -= 1 / i
#     else:
#         S_a += 1 / i
#     i += 1
# print(f"S_a = {S_a:.6f}")
# S_b = 0
# i = 2
# while i <= n + 1:
#     S_b += 1 / (i * (i - 1))
#     i += 1
# print(f"S_b = {S_b:.6f}")
# S_c = 0
# i = 2
# while i <= n + 1:
#     S_c += 1 / math.sqrt(i)
#     i += 1
# print(f"S_c = {S_c:.6f}")


# Nhập số nguyên dương n:2
# S_a = 0.500000
# S_b = 0.666667
# S_c = 1.284457





# Bài 4
# tu_so = int(input("Nhập tử số vào: "))
# mau_so = int(input("Nhập mẫu số vào: "))
# while mau_so ==0:
#     print(" Mẫu số lớn hơn 0 ")
#     mau_so = int(input("Nhập mẫu số : "))
# print(f"Phân số được nhập vào là: {tu_so}/{mau_so}")


# Nhập tử số vào: 2
# Nhập mẫu số vào: 3
# Phân số được nhập vào là 2/3



# Bài 5
# while True:
#     n = float(input("Nhập một số bất kỳ đến khi nhập số âm để dừng: "))
#     if n < 0:
#         break
# Nhập một số bất kỳ đến khi nhập số âm để dừng: 2
# Nhập một số bất kỳ đến khi nhập số âm để dừng: -3



# Bài 6
# n = int(input("Nhập một số: "))
# chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
# ket_qua = ""
# while n > 0:
#     ket_qua = chu_so[n % 10] + " " + ket_qua
#     n //= 10
# print("Kết quả:", ket_qua.strip())


# Nhập một số: 2837
# Kết quả: hai tám ba bảy 


# Bài 7
# a = int(input("Nhập số thứ nhất : "))
# b = int(input("Nhập số thứ hai : "))
# x, y = a, b
# while b != 0:
#     a, b = b, a % b
# ước_chung_lớn_nhất = a
# bội_chung_nhỏ_nhất = (x * y) // ước_chung_lớn_nhất 
# print("Bội chung nhỏ nhất là:", bội_chung_nhỏ_nhất)
# Nhập số thứ nhất: 2
# Nhập số thứ hai: 4
# Bội chung nhỏ nhất là: 4



# Bài 8
# kí_tự = ""
# while kí_tự == "":
#     kí_tự = input("Nhập một ký tự của bạn: ")
# mã_ascii = ord(kí_tự)
# print("Mã ASCII của", kí_tự, "là:", mã_ascii)
# Nhập một ký tự của bạn: 4
# Mã ASCII của 2 là: 52




# Bài 9
# n= int(input("Nhập một số: "))
# tong = 0
# while n > 0:
#     tong += n % 10 
#     n //= 10 
# print("Tổng các chữ số là:", tong)
# Nhập một số: 32
# Tổng các chữ số là: 5




# Bài 10
# số = input("Nhập một số thập phân: ")
# chữ_số = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
# kết_quả = ""
# i = 0 
# while i < len(số):
#     if số[i] != ".":
#         kết_quả += chữ_số[int(số[i])] + " "
#     i += 1  
# print("Kết quả:", kết_quả.strip())
# Nhập một số thập phân: 4.42
# Kết quả: bốn bốn hai 







# Bài 11
# print("Menu:")
# print("QUÁN NƯỚc LEM COFFEE ")
# print("1. Cafe")
# print("2. Cam vắt")
# print("3. Nước ép cà rốt")
# print("4. Nước lọc")
# print("5. Nước dừa")
# while True: 
#     lua_chon = float(input("Nhập lựa chọn của quý khách:  "))
#     if lua_chon == 1 :
#         print("Bạn đã oder  Cafe thành công ")
#     elif lua_chon == 2 :
#         print("Bạn đã oder  Cam vắt thành công")
#     elif lua_chon == 3 :
#         print("Bạn đã oder  Nước ép cà rốt thành công")
#     elif lua_chon == 4 :
#         print("Bạn đã oder  Nước lọc thành công")
#     elif lua_chon == 5 :
#         print("Bạn đã oder  Nước dừa thành công")
#     else  :
#         print("Bạn nhập quá lựa chọn vui lòng nhập lại nè")
#         break

# QUÁN NƯỚC LEM COFFEE
# 1. Cafe
# 2.Cam vắt 
# 3.Nước ép cà rốt 
# 4.Nước lọc 
# 5.Nước dừa
# Nhập lựa chọn của quý khách: 2
# Bạn đã oder Cam vắt thành công 

