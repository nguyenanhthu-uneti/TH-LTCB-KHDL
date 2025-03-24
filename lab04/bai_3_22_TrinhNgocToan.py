import math
n = int(input("Nhập số nguyên dương n: "))
while True:
    x = float(input("Nhập vào số thực x: "))
    cos_taylor = ((-1)**n * (x**(2*n))) / math.factorial(2*n)  
    cos_xap_xi = 1 - (x**2 / 2) 
    ket_qua = cos_taylor - cos_xap_xi 
    print("Kết quả:", ket_qua)
    if ket_qua <= 0.0001 :
        break
print(f"Số {n} và {x} thoả mãn điều kiện ")
# Nhập số nguyên dương n: 3
# Nhập vào số thực x: 60
# Kết quả: -64798201.0
# Số 3 và 60.0 thoả mãn điều kiện