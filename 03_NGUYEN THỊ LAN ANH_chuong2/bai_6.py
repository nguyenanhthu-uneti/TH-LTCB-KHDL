print("--MENU--")
print("1. Phim tinh cam")
print("2. Phim hoat hinh")
print("3. Phim kinh di")
print("4. Phim hanh dong")
while True:
    try:
        lua_chon = int(input("Nhap lua chon tu 1-4: "))
        if lua_chon<1 or lua_chon>4:
            print("Yeu cau nhap lua chon tu 1-4 !!")
            continue
    except ValueError:
        print("Yeu cau nhap dung hop le !!")
    else:
        if lua_chon == 1:
            print("Phim tinh cam")
        elif lua_chon == 2:
            print("Phim hoat hinh")
        elif lua_chon == 3:
            print("Phim kinh di")
        else:
            print("Phim hanh dong")
        break