ky_tu = input("Nhập một ký tự: ").lower()

if ky_tu.isalpha():
    if ky_tu in "aeiou":
        print("Ký tự là nguyên âm")
    else:
        print("Ký tự là phụ âm")
else:
    print("Đây không phải là ký tự trong bảng chữ cái tiếng Anh")