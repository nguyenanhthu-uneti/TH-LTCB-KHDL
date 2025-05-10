print("* Rap chieu phim CGV *")
print("1. phim hanh dong")
print("2. phim tinh cam")
print("3. phim hai")
print("4. phim hoat hinh")
print("5. phim kinh di")
lua_chon = int(input("Chon the loai phim ban muon xem: "))
if lua_chon == 1:
    print("Ban chon phim hanh dong")
elif lua_chon == 2:
    print("Ban chon phim tinh cam")
elif lua_chon == 3:
    print("Ban chon phim hai")
elif lua_chon == 4:
    print("Ban chon phim hoat hinh")
elif lua_chon == 5:
    print("Ban chon phim kinh di")
else:
    print("Khong co the loai phim nay")