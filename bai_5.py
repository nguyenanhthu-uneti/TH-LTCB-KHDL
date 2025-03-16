ky_tu = input("Nhập một ký tự: ")
ky_tu = ky_tu.lower()
if 'a' <= ky_tu <= 'z':
    if ky_tu in 'ueoai':
        print(f"'{ky_tu}' là nguyên âm.")
    else:
        print(f"'{ky_tu}' là phụ âm.")
else:
    print(f"'{ky_tu}' không phải là chữ cái tiếng Anh.")