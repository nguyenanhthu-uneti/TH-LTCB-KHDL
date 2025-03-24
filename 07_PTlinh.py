# Bai 1
def nhap_so_nguyen_duong():
    n = int(input("Nhập số nguyên dương n: "))
    while n <= 0:
        print("Vui lòng nhập số nguyên dương lớn hơn 0.")
        n = int(input("Nhập lại số nguyên dương n: "))
    return n

def tinh_tong(n):
    # S4 = 1^2 + 2^2 + ... + n^2
    S4 = 0
    i = 1
    while i <= n:
        S4 += i ** 2
        i += 1
    # S5 = 1^3 + 3^3 + 5^3 + ... + (2n+1)^3
    S5 = 0
    i = 1
    while i <= (2*n + 1):
        S5 += i ** 3
        i += 2
    # S6 = 2^4 + 4^4 + 6^4 + ... + (2n)^4
    S6 = 0
    i = 2
    while i <= (2*n):
        S6 += i ** 4
        i += 2

    return S4, S5, S6

n = nhap_so_nguyen_duong()
S4, S5, S6 = tinh_tong(n)

print(f"Tổng S4 = {S4}")
print(f"Tổng S5 = {S5}")
print(f"Tổng S6 = {S6}")
#input: 5
#output: Tổng S4 = 55
#       Tổng S5 = 2556
#       Tổng S6 = 15664

# Bai 2
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    print("Vui lòng nhập số nguyên dương lớn hơn 0.")
    n = int(input("Nhập lại số nguyên dương n: "))

S1 = 0
i = 1
while i <= n:
    if i % 2 == 0:
        S1 -= 1 / i
    else:
        S1 += 1 / i
    i += 1

S2 = 0
i = 2
while i <= n:
    if (i - 1) % 2 == 0:
        S2 += 1 / (i * (i + 1))
    else:
        S2 -= 1 / (i * (i + 1))
    i += 1

import math
S3 = 0
i = 2
while i <= n:
    if i % 2 == 0:
        S3 += 1 / math.sqrt(i)
    else:
        S3 -= 1 / math.sqrt(i)
    i += 1

print(f"Tổng S1 = {S1:.6f}")
print(f"Tổng S2 = {S2:.6f}")
print(f"Tổng S3 = {S3:.6f}")
#input: 4
#output: Tổng S1 = 0.583333
#       Tổng S2 = -0.133333
#       Tổng S3 = 0.629757

# Bai 4
def nhap_phan_so():
    tu = int(input("Nhập tử số: "))
    mau = int(input("Nhập mẫu số (khác 0): "))
    
    while mau == 0:  # Kiểm tra mẫu số có bằng 0 không
        print("Mẫu số không thể bằng 0. Vui lòng nhập lại!")
        mau = int(input("Nhập mẫu số (khác 0): "))
    
    return tu, mau

tu, mau = nhap_phan_so()
print(f"Phân số của bạn là: {tu}/{mau}")
#input: Nhập tử số là 3, nhập mẫu số là 2
#output: Phân số của bạn là: 3/2

# Bai 5
print("Nhập các số nguyên (nhập số âm để dừng):")

while True:
    n = int(input("Nhập số: "))  
    if n < 0:  # Nếu số nhập vào nhỏ hơn 0 thì dừng
        break
#input: 4, -99

# Bai 6
def number_to_words(number):
    digit_words = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    result = []
    while number > 0:
        result.insert(0, digit_words[number % 10])
        number //= 10
    return ' '.join(result) if result else 'không'

try:
    number = int(input("Nhập một số: "))
    if number < 0:
        print("Vui lòng nhập số nguyên không âm.")
    else:
        print("Số dưới dạng chữ:", number_to_words(number))
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
#input: 4
#output: Số dưới dạng chữ: bốn

# Bai 7
def tim_ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def tim_bcnn(a, b):
    return (a * b) // tim_ucln(a, b)

def main():
    while True:
        a = int(input("Nhập số nguyên dương thứ nhất: "))
        b = int(input("Nhập số nguyên dương thứ hai: "))
        if a > 0 and b > 0:
            break
        else:
            print("Vui lòng nhập hai số nguyên dương!")

    bcnn = tim_bcnn(a, b)
    print(f"Bội số chung nhỏ nhất của {a} và {b} là: {bcnn}")

main()
#input: Nhập số nguyên dương thứ nhất: 2
#       Nhập số nguyên dương thứ hai: 3
#output:Bội số chung nhỏ nhất của 2 và 3 là: 6

#Bai 8
def lay_gia_tri_ascii():
    while True:
        ky_tu = input("Nhập một ký tự: ")
        if len(ky_tu) == 1:  
            return ord(ky_tu)  
        else:
            print("Lỗi! Vui lòng nhập một ký tự duy nhất.")

def main():
    ascii_value = lay_gia_tri_ascii()
    print(f"Giá trị ASCII của ký tự là: {ascii_value}")

main()
#input: A
#output: Giá trị ASCII của ký tự là: 65

#Bai 9
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=" ")  
        a, b = b, a + b 
        count += 1

def main():
    while True:
        n = int(input("Nhập số nguyên dương n: "))
        if n > 0:
            break
        print("Vui lòng nhập số nguyên dương!")

    print(f"{n} số đầu tiên của dãy Fibonacci:")
    fibonacci(n)

main()
#input: 5
#output:0 1 1 2 3

#Bai 10
def so_sang_chu(n):
    chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    
    if n == 0:
        return "không"

    ket_qua = ""
    while n > 0:
        chu_so_hien_tai = n % 10  
        ket_qua = chu_so[chu_so_hien_tai] + " " + ket_qua 
        n //= 10  

    return ket_qua.strip()  

while True:
    try:
        n = int(input("Nhập một số nguyên dương: "))
        if n >= 0:
            break
        print("Vui lòng nhập số nguyên dương!")
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")

print(f"{n} là: {so_sang_chu(n)}")
#input: 6
#output: sáu

# Bai 11
def hien_thi_menu():
    print("Menu đồ uống:")
    print("1. Cafe")
    print("2. Cam vắt")
    print("3. Nước ép cà rốt")
    print("4. Nước lọc")
    print("5. Nước dừa")

def chon_do_uong():
    while True:
        try:
            lua_chon = int(input("Nhập số tương ứng với đồ uống bạn muốn chọn (1-5): "))
            if 1 <= lua_chon <= 5:
                return lua_chon
            else:
                print("Vui lòng nhập số từ 1 đến 5!")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ!")

def hien_thi_ket_qua(lua_chon):
    do_uong = {
        1: "Cafe",
        2: "Cam vắt",
        3: "Nước ép cà rốt",
        4: "Nước lọc",
        5: "Nước dừa"
    }
    print(f"Bạn đã chọn: {do_uong[lua_chon]}")

def main():
    hien_thi_menu()
    lua_chon = chon_do_uong()
    hien_thi_ket_qua(lua_chon)

main()
#input: 2
#output: Bạn đã chọn: Cam vắt