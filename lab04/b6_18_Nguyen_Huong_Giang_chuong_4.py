# 6. Viết chương trình nhập một số từ bàn phím và in ra màn hình bằng chữ.
# Ví dụ 1234, kết quả in ra màn hình là một hai ba bốn.
 

chu_so_sang_chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
so = input("Nhập số: ")
if not so.isdigit():
    print("Vui lòng nhập lại ")
else:
    ket_qua = ""
    i = 0
    while i < len(so):
        chu_so = int(so[i]) 
        ket_qua += chu_so_sang_chu[chu_so] + " "  
        i += 1
    
    print("Kết quả:", ket_qua)

# input : Nhập số  345
# output : ba bốn năm