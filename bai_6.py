print("* Rạp chiếu phim ABC *")
print("1.Phim hành động")
print("2.Phim tình cảm")
print("3.Phim hoạt hình")
print("4.Phim khoa hoc vien tuong")
print("5.Phim kinh dị")
lua_chon = int(input("Vui lòng nhập số để chọn phim: "))
if lua_chon == 1:
    print("Bạn đã chọn phim hành động")
elif lua_chon == 2:
    print("Bạn đã chọn phim tình cảm")
elif lua_chon == 3:
    print("Bạn đã chọn phim hoạt hình")
elif lua_chon == 4:
    print("Bạn đã chọn phim khoa hoc vien tuong")
elif lua_chon == 5:
    print("Bạn đã chọn phim kinh dị")
else:
    print("Không có phim này trong danh sách")