
ki_tu = input("Nhập một ký tự: ")
nguyen_am = "aeiou"

if ki_tu.isalpha() and len(ki_tu) == 1:  
    if ki_tu in nguyen_am:
        print(f"{ki_tu} là nguyên âm.")
    else:
        print(f"{ki_tu} là phụ âm.")
else:
    print("Ký tự không hợp lệ. Vui lòng nhập một chữ cái.")