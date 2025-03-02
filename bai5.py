c = input("nhap ki tu: ")

if 'a' <= c <= 'z':
    if c in 'aeiou':
        print("nguyen am")
    else:
        print("phu am")
else:
    print("ko phai ki tu trong bang chu cai")
