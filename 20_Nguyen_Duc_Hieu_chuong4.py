#Bài1
while True:
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n > 0:
            break
        else:
            print("Vui lòng nhập số nguyên dương lớn hơn 0.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
S4 = 0
i = 1
while i <= n:
    S4 += i ** 2
    i += 1
S5 = 0
i = 0
while i < n:
    S5 += (2 * i + 1) ** 3
    i += 1
S6 = 0
i = 1
while i <= n:
    S6 += (2 * i) ** 4
    i += 1
print(f"S4 = {S4}")
print(f"S5 = {S5}")
print(f"S6 = {S6}")
#nhập n=3 in ra màn hình s4=14 s5=153 s6=1586


#Bài2
import math
n = int(input("Nhập số nguyên dương n: "))
S1 = 0
i = 1
while i <= n:
    if i % 2 == 0:
        S1 -= 1 / i
    else:
        S1 += 1 / i
    i += 1
S2 = 0
i = 1
while i <= n:
    S2 += 1 / (i * (i + 1))
    i += 1
S3 = 0
i = 2
while i <= n:
    S3 += 1 / math.sqrt(i)
    i += 1
print(f"S1 = {S1}")
print(f"S2 = {S2}")
print(f"S3 = {S3}")
#nhập n=3 in ra màn hình s1=0.8333333333333 s2=0.75 s3=1.2844570503761732 



#Bài3
import math
x = float(input("Nhập giá trị x (radian): "))
epsilon = 1e-4
cos_x_taylor = 1
term = 1  
n_taylor = 1  
while abs(term) > epsilon:
    term *= -x**2 / ((2 * n_taylor) * (2 * n_taylor - 1))  
    cos_x_taylor += term  
    n_taylor += 1 
n = 1  
while True:
    if n < 2:  
        n += 1
        continue
    cos_x_approx = 1 - (x**2) / (n * (n - 1))  
    if abs(cos_x_approx - cos_x_taylor) < epsilon:  
        break
    n += 0.1 
print(f"Giá trị nhỏ nhất của n thỏa mãn điều kiện là: {n}")
#Nhập giá trị x (radian): 0.2
#Giá trị nhỏ nhất của n thỏa mãn điều kiện là: 2

#Bài4
tu_so = int(input("Nhập tử số: "))
while True:
    mau_so = int(input("Nhập mẫu số: "))
    if mau_so != 0:
        break
    print("Mẫu số không thể bằng 0. Vui lòng nhập lại.")
phan_so = tu_so / mau_so
print(f"Phân số {tu_so}/{mau_so} có giá trị: {phan_so:.4f}")
#nhập tử số=4 mẫu=0 in ra màn hình mẫu số ko thể bằng 0 vui lòng nhập lại



#Bài5
numbers = []
while True:
    num = float(input("Nhập một số (nhập số âm để dừng): "))
    if num < 0:
        break  
    numbers.append(num)
print("Các số đã nhập:", numbers)
# Nhập một số (nhập số âm để dừng): 5
# Nhập một số (nhập số âm để dừng): 4
# Nhập một số (nhập số âm để dừng): 3
# Nhập một số (nhập số âm để dừng): 8
# Nhập một số (nhập số âm để dừng): -6
# Các số đã nhập: [5.0, 4.0, 3.0, 8.0]

#Bài6
so_sang_chu = {
    '0': "Không", '1': "Một", '2': "Hai", '3': "Ba", '4': "Bốn",
    '5': "Năm", '6': "Sáu", '7': "Bảy", '8': "Tám", '9': "Chín"
}
num = input("Nhập số nguyên: ")
while not num.isdigit(): 
    print("Vui lòng nhập số nguyên dương hợp lệ.")
    num = input("Nhập số nguyên: ")
ket_qua = " ".join(so_sang_chu[ch] for ch in num)
print(f"Số {num} đọc là: {ket_qua}")
#Nhập số nguyên: 567
#Số 567 đọc là: Năm Sáu Bảy



#Bài7
a = int(input("Nhập số nguyên dương thứ nhất: "))
b = int(input("Nhập số nguyên dương thứ hai: "))
x, y = a, b
while y != 0:
    x, y = y, x % y 
bcnn = abs(a * b) // x
print(f"BCNN({a}, {b}) = {bcnn}")
#Nhập số nguyên dương thứ nhất: 8
#Nhập số nguyên dương thứ hai: 4
#BCNN(8, 4) = 8



#Bài8
while True:
    char = input("Nhập một ký tự bất kỳ: ")
    if len(char) == 1:
        ascii_value = ord(char)  
        print(f"Giá trị ASCII của '{char}' là: {ascii_value}")
        break  
    else:
        print("Vui lòng chỉ nhập một ký tự!")
#Nhập một ký tự bất kỳ: B
#Giá trị ASCII của 'B' là: 66




#Bài9
n = int(input("Nhập một số nguyên dương: "))
tong = 0
temp = n

while temp > 0:
    tong += temp % 10  
    temp //= 10 
print(f"Tổng các chữ số của {n} là: {tong}")
#Nhập một số nguyên dương: 1234
#Tổng các chữ số của 1234 là: 10




#Bài10
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
num = float(input("Nhập một số thập phân: "))
chuoi_so = str(num)
ket_qua = ""
for chu in chuoi_so:
    if chu.isdigit():
        ket_qua += chu_so[int(chu)] + " "
    elif chu == ".":  
        ket_qua += "phẩy "
print(f"Số {num} khi chuyển đổi thành chữ là: {ket_qua.strip()}")
#Nhập một số thập phân: 3.354
#Số 3.354 khi chuyển đổi thành chữ là: ba phẩy ba năm bốn


 #Bài11
print("=== MENU ĐỒ UỐNG ===")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt")
print("4. Nước lọc")
print("5. Nước dừa")
while True:
     choice = input("Nhập số để chọn đồ uống (1-5): ")

     if choice == "1":
         print("Bạn đã chọn: Cafe")
         break
     elif choice == "2":
         print("Bạn đã chọn: Cam vắt")
         break
     elif choice == "3":
         print("Bạn đã chọn: Nước ép cà rốt")
         break
     elif choice == "4":
         print("Bạn đã chọn: Nước lọc")
         break
     elif choice == "5":
         print("Bạn đã chọn: Nước dừa")
         break
     else:
         print("Số không hợp lệ! Vui lòng nhập lại từ 1 đến 5.")
# # === MENU ĐỒ UỐNG ===
# # 1. Cafe
# # 2. Cam vắt
# # 3. Nước ép cà rốt
# # 4. Nước lọc
# # 5. Nước dừa
# # Nhập số để chọn đồ uống (1-5): 4
# # Bạn đã chọn: Nước lọc