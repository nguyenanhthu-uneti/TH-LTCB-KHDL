n = int(input("Nhap vao so nguyennguyen: "))
tong = 0
while n > 0:
    tong += n % 10
    n //= 10 
print("Tong cac chu so la:", tong)