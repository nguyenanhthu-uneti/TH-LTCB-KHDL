
#bai1
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    print("Vui lòng nhập số nguyên dương lớn hơn 0.")
    n = int(input("Nhập lại số nguyên dương n: "))
S4 = 0
i = 1
while i <= n:
    S4 += i ** 2
    i += 1


S5 = 0
i = 1
while i <= (2 * n + 1):
    S5 += i ** 3
    i += 2


S6 = 0
i = 2
while i <= (2 * n):
    S6 += i ** 4
    i += 2


print(f"Tổng S4 = {S4}")
print(f"Tổng S5 = {S5}")
print(f"Tổng S6 = {S6}")
#input:6
#output:Tổng S4 = 91
# Tổng S5 = 4753
# Tổng S6 = 36400
# Tính tổng S4 = 1^2 + 2^2 + ... + n^2
#bai2 

def nhap_n():
    n = int(input("Nhập số nguyên dương n: "))
    while n <= 0:
        n = int(input("Nhập lại số nguyên dương n: "))
    return n


def can_bac_hai(x):
    guess = x
    epsilon = 1e-6  # Sai số nhỏ
    while abs(guess * guess - x) > epsilon:
        guess = (guess + x / guess) / 2
    return guess


def tinh_S1(n):
    S1 = 0
    i = 1
    while i <= n:
        S1 += (-1) ** (i + 1) / i
        i += 1
    return S1


def tinh_S2(n):
    S2 = 0
    i = 2
    while i <= n:
        S2 += (-1) ** (i + 1) / (i * (i + 1))
        i += 1
    return S2


def tinh_S3(n):
    S3 = 0
    i = 2
    while i <= n:
        S3 += (-1) ** i / can_bac_hai(i)  
        i += 1
    return S3

# Chương trình chính
n = nhap_n()
print(f"S1 = {tinh_S1(n):.6f}")
print(f"S2 = {tinh_S2(n):.6f}")
print(f"S3 = {tinh_S3(n):.6f}")
#input:6
#output:S1 = 0.616667
# S2 = -0.123810
# S3 = 0.590791
#bai5
print("Nhập các số nguyên (nhập số âm để dừng):")

while True:
    n = int(input("Nhập số: "))
    if n < 0:  
        break
#input : 6 , -2

#bai7

def tim_ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def tim_bcnn(a, b):
    return (a * b) // tim_ucln(a, b)

# Nhập hai số nguyên dương
a = int(input("Nhập số nguyên dương thứ nhất: "))
b = int(input("Nhập số nguyên dương thứ hai: "))

# Tính và in kết quả
bcnn = tim_bcnn(a, b)
print(f"Bội số chung nhỏ nhất của {a} và {b} là: {bcnn}")
#input :Nhập số nguyên dương thứ nhất: 6
# Nhập số nguyên dương thứ hai: 3
# output : Bội số chung nhỏ nhất của 6 và 3 là: 6
#bai6

chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]


so = input("Nhập một số: ")


ket_qua = " ".join(chu_so[int(c)] for c in so)


print("Số bằng chữ:", ket_qua)
#input:23
#output:Số bằng chữ: hai ba
#bai8 

while True:
    ky_tu = input("Nhập một ký tự: ")
    
    if len(ky_tu) == 1: 
        break
    else:
        print("Lỗi! Vui lòng nhập một ký tự duy nhất.")


ascii_value = ord(ky_tu)
print(f"Giá trị ASCII của '{ky_tu}' là: {ascii_value}")
#input:L
#output:Giá trị ASCII của 'L' là: 76
#bai9

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
#input:6
#output:6 số đầu tiên của dãy Fibonacci:
# 0 1 1 2 3 5
#bai10
def so_sang_chu(n):
    # Danh sách chữ số dưới dạng chữ
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
#input:6
#output:6 là: sáu
#bai11
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
#input:1
#output:Menu đồ uống:
# 1. Cafe
# 2. Cam vắt
# 3. Nước ép cà rốt
# 4. Nước lọc
# 5. Nước dừa
# Nhập số tương ứng với đồ uống bạn muốn chọn (1-5): 1
# Bạn đã chọn: Cafe
#bai4

tu = int(input("Nhập tử số: "))


mau = int(input("Nhập mẫu số (khác 0): "))
while mau == 0:
    print("Lỗi! Mẫu số không thể bằng 0. Vui lòng nhập lại.")
    mau = int(input("Nhập mẫu số (khác 0): "))


print(f"Phân số bạn nhập là: {tu}/{mau}")
#input:Nhập tử số: 6
# Nhập mẫu số (khác 0): 7
#output:Phâ số bạn nhập là: 6/7