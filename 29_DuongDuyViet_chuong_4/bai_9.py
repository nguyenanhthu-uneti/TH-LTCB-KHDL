while True:
    n = input("Nhập một số nguyên dương: ")
    
    # Kiểm tra nếu người dùng nhập số hợp lệ (chỉ chứa chữ số)
    if n.isdigit():  # kiểm tra xem chuỗi có phải là số hay không
        n = int(n)  # chuyển chuỗi thành số nguyên
        break
    else:
        print("Vui lòng nhập một số nguyên dương hợp lệ.")

# Tính tổng các chữ số
sum_digits = 0
for digit in str(n):  # chuyển số thành chuỗi để dễ dàng duyệt từng ký tự
    sum_digits += int(digit)  # chuyển từng ký tự thành số nguyên và cộng vào tổng

# Hiển thị kết quả
print(f"Tổng các chữ số của số {n} là: {sum_digits}")
