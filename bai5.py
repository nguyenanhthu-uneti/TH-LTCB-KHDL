# Nhập một ký tự từ người dùng
char = input("Nhập ký tự trong bảng tiếng Anh: ").lower()

# Danh sách các nguyên âm
vowels = 'aeiou'

# Kiểm tra xem ký tự có phải là nguyên âm hay không
if char in vowels:
    print(f"{char} là nguyên âm")
else:
    print(f"{char} là phụ âm")
