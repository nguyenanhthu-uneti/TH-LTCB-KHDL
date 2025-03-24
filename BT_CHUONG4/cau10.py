số = input("Nhập một số thập phân: ")
chữ_số = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
kết_quả = ""
i = 0 
while i < len(số):
    if số[i] != ".":
        kết_quả += chữ_số[int(số[i])] + " "
    i += 1  
print("Kết quả:", kết_quả.strip())