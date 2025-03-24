# #bai7
n = int(input("nhập giá trị  : "))
if n <= 0 :
    print("vui lòng nhập lại")
else :
    tong = 0
    for i in range(1,n+1):
        tong+= 1/i
print(f"giá trị là :{tong}")

# #bai8 
n = int(input("nhập giá trị n : "))
tong_1 = 0 
for i in range(1,n+1) : 
    tong_1 += i 
tong_2 = 0    
for a in range(1,2*n , 2):
    tong_2 += a
tong_3 = 0
for l in range(2,2*n + 1 ,2):
    tong_3+=l
print(f"Tổng S1 = {tong_1}")
print(f"Tổng S2 = {tong_2}")
print(f"Tổng S3 = {tong_3}") 
#bai9 
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    print("Số nhập vào không hợp lệ, vui lòng nhập lại!")
    n = int(input("Nhập số nguyên dương n: "))

S4 = 0
for i in range(1, n + 1):
    S4 += i ** 2 
    
S5 = 0
for i in range(1, 2*n, 2):
    S5 += i ** 3 
    
S6 = 0
for i in range(2, 2*n + 1, 2):  
    S6 += i ** 4
print(f"Tổng S4 = {S4}")
print(f"Tổng S5 = {S5}")
print(f"Tổng S6 = {S6}")    
#bai10
def phan_tich_thua_so_nguyen_to(n):
    """Hàm phân tích số nguyên n thành thừa số nguyên tố"""
    ket_qua = []
    for i in range(2, n + 1):  
        while n % i == 0:  
            ket_qua.append(i)
            n //= i  
        if n == 1:  
            break
    return ket_qua
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    print("Số nhập vào không hợp lệ, vui lòng nhập lại!")
    n = int(input("Nhập số nguyên dương n: "))
thua_so = phan_tich_thua_so_nguyen_to(n)
phan_tich = " * ".join(map(str, thua_so))
print(f"Phân tích thừa số nguyên tố của {n} là: {phan_tich}")
#bai11
#a
def ve_tam_giac_can(n):
    """Vẽ tam giác sao rỗng cân với chiều cao n"""
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end=" ")
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i or i == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print()  
n = int(input("Nhập số hàng của tam giác: "))
while n <= 0:
    print("Số nhập vào không hợp lệ, vui lòng nhập lại!")
    n = int(input("Nhập số hàng của tam giác: "))
ve_tam_giac_can(n)
#b
def ve_tam_giac_b(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i or i == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print() 
n = int(input("Nhập số hàng của tam giác: "))
while n <= 0:
    print("Số nhập vào không hợp lệ, vui lòng nhập lại!")
    n = int(input("Nhập số hàng của tam giác: "))
ve_tam_giac_b(n)
#c
def ve_tam_giac_deu_kin(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print() 
n = int(input("Nhập số hàng của tam giác: "))
while n <= 0:
    print("Số nhập vào không hợp lệ, vui lòng nhập lại!")
    n = int(input("Nhập số hàng của tam giác: "))
ve_tam_giac_deu_kin(n)

