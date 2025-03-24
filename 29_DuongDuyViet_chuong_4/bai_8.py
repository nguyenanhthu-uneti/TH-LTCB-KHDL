while True:
    n = input("Nhập một ký tự ( nhập 'thoat' để thoát chương trình)  : ")
    if len(n) == 1:
        ascii_value = ord(n)
        print(f"Giá trị ASCII của ký tự '{n}' là: {ascii_value}")
    elif n == 'thoat':
        break
    else:
        print("Vui lòng chỉ nhập một ký tự.")
