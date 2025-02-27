print("Menu")
print("1, Kinh di")
print("2,Tinh cam")
print("3,trinh tham")
print("0,Thoat")
while True:
    a=int(input("Nhap so: "))
    if a==1:
        print("Ban chon Kinh di")
    elif a==2:
        print("Ban chon Tinh cam")
    elif a==3:
        print("Ban chon trinh tham")
    elif a==0:
        print("Ban chon thoat")
        break
    else:
        print("Ban chon sai, moi chon lai")