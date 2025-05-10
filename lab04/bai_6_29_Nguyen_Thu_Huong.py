# Viết chương trình nhập một số từ bàn phím và in ra màn hình bằng chữ.
# Ví dụ 1234, kết quả in ra màn hình là một hai ba bốn.
n = int(input("Nhập một số: "))
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
ket_qua = ""
while n > 0:
    ket_qua = chu_so[n % 10] + " " + ket_qua
    n //= 10
print("Kết quả:", ket_qua.strip())
#  input :Nhập một số: 234 
# output :Kết quả: hai ba bốn
