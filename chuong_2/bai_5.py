n = input("Nhập 1 ký tự: ").lower()
if n.isalpha():
    if n in "ueoai":
        print(f"{n} là nguyên âm")
    else:
        print(f"{n} là phụ âm")
else:
    print("Ký tự không hợp lệ,nhập lại!")
