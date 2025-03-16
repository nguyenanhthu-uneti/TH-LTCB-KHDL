# 10. Viết chương trình nhập một số thập phân và sau đó chuyển đổi số đó thành dạng ký tự. Ví dụ: 324 là ba hai bon.

so = int(input("Nhập vào số thập phân: "))
chuoi_so = str(so)
ket_qua = ""
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
i = 0
while i < len(chuoi_so):
    ket_qua += chu_so[int(chuoi_so[i])] + " "
    i += 1

print("Dạng chữ: ", ket_qua.strip())
 
# input: Nhập vào số thập phân 324
# output : ba hai bốn