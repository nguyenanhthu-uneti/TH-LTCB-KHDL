a=input("nhap ký tự: ")
a=a.lower()
nguyen_am="ueoai"
if a in nguyen_am:
    print(f"{a} là nguyên âm")
elif a.isalpha():
    print(f"{a} là phụ âm")
else:
    print("nhập sai")
