# Viết chương trình nhập một số và tính tổng các chữ số của số vừa nhập rồi hiển thị
# kết quả.
n= int(input("Nhập một số: "))
tong = 0
while n > 0:
    tong += n % 10 
    n //= 10 
print("Tổng các chữ số là:", tong)
# Nhập một số: 12
# Tổng các chữ số là: 3