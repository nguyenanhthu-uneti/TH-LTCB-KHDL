n=input("Nhap ky tu: ")
if n.isalpha()==True:
    if n=='a' or n=='e' or n=='i' or n=='o' or n=='u' or n=='y':
        print("Do la nguyen am")
    else:
        print("Do la phu am")
else:
    print("Nhap ki tu")