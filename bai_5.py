ky_tu = input("Nhập một ký tự: ")
if ky_tu[:1] == "" or ky_tu[1:]:  
    print("Vui lòng nhập đúng một ký tự.")
elif not ('A' <= ky_tu <= 'Z' or 'a' <= ky_tu <= 'z'): 
    print(f"'{ky_tu}' không phải là ký tự chữ cái")
else:
    if ky_tu.lower() in 'aeiou':
        print(f"'{ky_tu}' là nguyên âm")
    else:
        print(f"'{ky_tu}' là phụ âm")