ky_tu = input("Nhap ky tu: ")
ky_tu = ky_tu.lower()
if not 'a' <= ky_tu <= 'z':
    print(f"{ky_tu} khong phai la chu cai tieng anh")
else:
    nguyen_am = ['a', 'e', 'i', 'o', 'u']
    if ky_tu in nguyen_am:
        print(f"{ky_tu} la nguyen am")
    else:
        print(f"{ky_tu} la phu am")