# 9. Viết chương trình nhập một số và tính tổng các chữ số của số vừa nhập rồi hiển thị kết quả.


so = int(input("Nhập một số nguyên: "))
tong = 0
while so > 0:
    chu_so = so % 10
    tong += chu_so  
    so //= 10  

print("Tổng các chữ số của số vừa nhập là:", tong)
# input:Nhập một số nguyên 55
# Tổng các chữ số của số vừa nhập là : 10
