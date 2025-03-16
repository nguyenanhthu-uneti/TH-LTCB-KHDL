#Bai1: 
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    print("Vui lòng nhập lại số nguyên dương!")
    n = int(input("Nhập số nguyên dương n: "))

#Tính tổng S4 = 1^2 + 2^2 + ... + n^2
S4 = 0
i = 1
while i <= n:
    S4 += i ** 2
    i += 1
print(f"Tổng S4 = {S4}")

#Tính tổng S5 = 1^3 + 3^3 + ... + (2n+1)^3
S5 = 0
i = 1
while i <= (2 * n + 1):
    S5 += i ** 3
    i += 2
print(f"Tổng S5 = {S5}")

#Tính tổng S6 = 2^4 + 4^4 + ... + (2n)^4
S6 = 0
i = 2
while i <= (2 * n):
    S6 += i ** 4
    i += 2
print(f"Tổng S6 = {S6}")

#input: 8
#output: S4=204, S5=13041, S6=140352 

#Bai2:
import math
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    print("Vui lòng nhập lại số nguyên dương!")
    n = int(input("Nhập số nguyên dương n: "))

#Tính tổng S = 1 - 1/2 + 1/3 - 1/4 + 1/5 - ...
S_a = 0
i = 1
while i <= n:
    if i % 2 == 0:
        S_a -= 1 / i
    else:
        S_a += 1 / i
    i += 1
print(f"Tổng S = {S_a:.5f}")
#Tính tổng S = 1/2 + 1/(2.3) + 1/(3.4) + ...
S_b = 0
i = 2
while i <= n:
    S_b += 1 / (i * (i + 1))
    i += 1
print(f"Tổng S = {S_b:.5f}") 
#Tính tổng S = 1/căn(2) + 1/căn(3) + 1/căn(4) + ...
S_c = 0
i = 2
while i <= n:
    S_c += 1 / math.sqrt(i)
    i += 1
print(f"Tổng S = {S_c:.5f}")

#input: 8
#output: S_a=0.78333, S_b=0.33333, S_c=2.2316723167

#Bai3:

#Bai4: 
tu_so = int(input("Nhập vào tử số: "))
mau_so = int(input("Nhập vào mẫu số: "))
while mau_so == 0:
    print("Mẫu số phải khác 0!")
    mau_so = int(input("Nhập mẫu số (khác 0): "))
print(f"Phân số bạn đã nhập là: {tu_so}/{mau_so}")

#input: 2, 6
#output: 2/6 

#Bai5:

while True:
    so = int(input("Nhập một số bất kỳ (nhập số âm để dừng): "))
    if so < 0:
        print("Đã nhập số âm, chương trình kết thúc.")
        break

#input: -2
#output: Đã nhập số âm, chương trình kết thúc

#Bai6: 
so_sang_chu = {
    '0': "không", '1': "một", '2': "hai", '3': "ba", '4': "bốn",
    '5': "năm", '6': "sáu", '7': "bảy", '8': "tám", '9': "chín"
}

so = input("Nhập một số: ")
ket_qua = ""
i = 0
while i < len(so):
    if so[i] in so_sang_chu:  
        ket_qua += so_sang_chu[so[i]] + " "
    i += 1
print("Kết quả:", ket_qua.strip())  

#input: 2811
#output: hai tám một một 

#Bai7: 

a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
bcnn = max(a, b)
while True:
    if bcnn % a == 0 and bcnn % b == 0:  
        break  
    bcnn += 1  

print("Bội chung nhỏ nhất của", a, "và", b, "là:", bcnn)

#input: 4,6
#output: Bội chung nhỏ nhất của 4 và 6 là: 12

#Bai8:

while True:
    ky_tu = input("Nhập một ký tự bất kỳ (nhập '0' để thoát): ")

    if ky_tu == '0':  
        print("Kết thúc chương trình.")
        break
    
    if len(ky_tu) != 1:  
        print("Vui lòng nhập chỉ một ký tự!")
        continue

    print(f"Giá trị ASCII của '{ky_tu}' là: {ord(ky_tu)}")

#input: A,@,0
#output: 65,64,Kết thúc chương trình

#Bài9:

so = int(input("Nhập một số nguyên dương: "))

tong = 0  

while so > 0:
    chu_so = so % 10  
    tong += chu_so  
    so //= 10  

print("Tổng các chữ số là:", tong)

#input: 2811
#output: Tổng các chữ số là: 12

#Bai10:

chu_so_text = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

so = int(input("Nhập một số nguyên dương: "))

chuoi_ket_qua = ""  

while so > 0:
    chu_so = so % 10  
    chuoi_ket_qua = chu_so_text[chu_so] + " " + chuoi_ket_qua  
    so //= 10 

print("Dạng ký tự:", chuoi_ket_qua.strip())


#input: 324
#output: ba hai bốn 

#Bai11:

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

