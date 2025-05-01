
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]


so_nhap = input("Nhập một số: ")


if so_nhap.isdigit():
    i = 0
    ket_qua = ""
    
    while i < len(so_nhap):
        chu = so_nhap[i]  
        ket_qua += chu_so[int(chu)] + " "
        i += 1 
    
    print("Kết quả:", ket_qua.strip())
else:
    print("Vui lòng nhập một số hợp lệ.")
