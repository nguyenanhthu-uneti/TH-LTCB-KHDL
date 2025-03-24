# #bài 1
# n = int(input("nhập số năm cần kiểm tra: "))
# if n > 0:
#     if n % 4 == 0 and n % 100!= 0:
#         print(f"{n} là năm nhuận")
#     elif n% 400 ==0:
#         print(f"{n}là năm nhuận ")
# else:
#     print(f"{n} là năm nhuận ")








# #bài 2
# x = float(input("nhập tọa độ x vào điểm M: "))
# y = float(input("nhập tạo độ y vào điểm N: "))
# a = float(input("nhập tọa độ a vào tâm I: "))
# b = float(input("nhập tọa độ b vào tâm I: "))
# R = float(input("nhập vào bán kính R: "))
# d = ((x - a) **2 + ((y-b) ** 2)) / 1/2
# if d <= R and d==R:
#     print(True)
# else:
#     print(False) 






# #bài 3
# a = float(input("nhập vào số a: "))
# b = float(input("nhập vào số b: "))
# c = float(input("nhập vào số c: "))
# #
# if a > 0 and b>0 and c > 0:
#     if a + b > c or b + c > a or a+ c > b:
#         print("ba cạnh a,b,c tạo thành một tam giác")
#     else:
#         if a == b ==c:
#             print("tam giác đều ")
#         elif a == b or a == c or b == c:
#             print("tam giác cân ")
#         elif a ** 2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
#             print("tam giác vuông")
#         else:
#             print("tam giác thường ")
# else:
#    print("ba cạnh không phải là tam giác")








# #bài 4
# a = float(input("nhập vào sô a: "))
# b = float(input("nhập vào sô b: "))
# c =  float(input("nhập vào sô c: "))
# if a>= b and a >= c :
#     print("a là số lớn nhất ")
# elif b>= a and b >= c:
#     print("b là số lớn nhất ")
# else:
#     print("c là số lớn nhất ")








# #bài 5 
# ki_tu = str(input("nhập kí tự bất kì trong bảng chữ cái : "))
# if ki_tu == "u" or ki_tu == "e" or ki_tu == "o" or ki_tu== "a" or ki_tu=="i":
#     print(f"{ki_tu} là nguyên âm")
# else:
#     print(f"{ki_tu}là phụ âm ")









# #bài 6 
# print("nhập lựa chọn của bạn ")
# print("1. phim kinh dị ")
# print("2.phim hành động")
# print("3.phim khoa học viễn tưởng ")
# print("4.phim hoạt hình ")
# n = int(input("nhập thứ tự phim bạn muốn xem: "))
# if n == 1:
#     print("1. phim kinh dị ")
# elif n ==2:
#     print("2. phim hành động")
# elif n == 3:
#     print("3.phim khoa hoạc viễn tưởng ")
# elif n == 4:
#     print("4.phim hoạt hình ")
# else:
#     print("lựa chọn lại")








# #bài 8
# n = input("nhập số điểm: ")
# if n == "A":
#     print("sinh viên loại xuất sắc")
# elif n == "B":
#     print("sinh viên loại giỏi ")
# elif n == "C":
#     print("sinh viên loại khá")
# elif n == "D":
#     print("sinh viên loại trung bình ")
# elif n == "E":
#     print("sinh viên loại yếu ")
# elif n == "F":
#     print("sinh viên loại kém ")
# else:
#     print("yêu cầu nhập lại ")









# #bài 10
# n = int(input("nhập số lương của nhân viên :"))
# if n >= 15000000:
#     phi_thue = 0.3
# elif n >= 7000000 and n <= 15000000:
#     phi_thue = 0.2
# elif n <= 7000000:
#     phi_thue = 0.1
# thue = n * phi_thue
# luong_thuc_te = n - phi_thue
# print(f"thuế của nhân viên là: {thue} ")
# print(f"lương thực tế của nhân viên là: {luong_thuc_te}")









# #bài 11
# n = int(input("nhập tháng cần tìm: "))
# if n == 1 or n == 3 or n == 5 or n== 7 or n== 8 or n == 10 or n == 12:
#     print(f"tháng {n} có 31 ngày ")
# elif n == 4 or n == 6 or n == 9 or n == 11:
#     print(f"tháng {n} có 30 ngày ")
# elif n == 2:
#     print(f"tháng {n} có 28 hoặc 29 ngày ")
# else:
#     print("vui lòng nhập lại tháng ")










# #bài 16 
# a = int(input("nhập số hàng trăm: "))
# b = int(input("nhập số hàng chục: "))
# c = int(input("nhập số hàng đơn vị: "))
# if a != 0 or b !=0 or c !=0:
#     print(f"{a} trăm {b} mươi {c}")
# elif a != 0 or b == 0 or c !=0:
#     print(f"{a} trăm linh {c}")
# elif a != 0 or b != 0 or c ==0:
#     print(f"{a} trăm {b} mươi")
# elif a !=0 or b == 0 or c == 0:
#     print(f"{a} trăm")







#bài 18
n = float(input("nhập thâm niên công tác của nhân viên : "))
if n < 12:
    he_so = 2.34
elif n >= 12 and n < 36:
    he_so = 3.33
elif n>= 36 and n< 60:
    he_so = 3.66
elif n >= 60:
    he_so = 3.99
luong_co_ban = 1350000
luong = he_so * luong_co_ban
print(f"luong của nhân viên là: {luong}")
