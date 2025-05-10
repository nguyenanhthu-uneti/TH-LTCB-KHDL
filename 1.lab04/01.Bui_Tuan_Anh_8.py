while True:
    c = input("Nhập một ký tự: ")
    if c: 
        print("Mã ASCII của", c[0], "là:", ord(c[0]))
        break 
    else:
        print("Vui lòng nhập ít nhất một ký tự!")  # Yêu cầu nhập lại nếu bỏ trống
