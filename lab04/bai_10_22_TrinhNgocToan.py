# Viết chương trình nhập một số thập phân và sau đó chuyển đổi số đó thành dạng ký
# tự. Ví dụ: 324 là ba hai bon.
số = input("Nhập một số thập phân: ")
chữ_số = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
kết_quả = ""
i = 0 
while i < len(số):
    if số[i] != ".":
        kết_quả += chữ_số[int(số[i])] + " "
    i += 1  
print("Kết quả:", kết_quả.strip())
# Nhập một số thập phân: 3.14
# Kết quả: ba một bốn