chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

so_nhap = input("Nhập một số: ")

while not so_nhap.isdigit():  # Kiểm tra nhập đúng số nguyên
    so_nhap = input("Vui lòng nhập số hợp lệ: ")

ket_qua = ""
i = 0

while i < len(so_nhap):  # Duyệt từng chữ số và chuyển thành chữ
    ket_qua += chu_so[int(so_nhap[i])] + " "
    i += 1

print("Kết quả:", ket_qua.strip())


# Nhập một số: 68
# Kết quả: sáu tám