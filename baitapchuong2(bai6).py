print("Chào mừng đến với rạp chiếu phim ABC!")
print("Danh sách thể loại phim:")
print("1. Hành động")
print("2. Kinh dị")
print("3. Hài hước")
print("4. Tình cảm")
print("5. Khoa học viễn tưởng")

lua_chon = input("Nhập số tương ứng với thể loại phim bạn muốn xem: ")

if lua_chon == "1":
    print("Bạn đã chọn phim thể loại Hành động.")
elif lua_chon == "2":
    print("Bạn đã chọn phim thể loại Kinh dị.")
elif lua_chon == "3":
    print("Bạn đã chọn phim thể loại Hài hước.")
elif lua_chon == "4":
    print("Bạn đã chọn phim thể loại Tình cảm.")
elif lua_chon == "5":
    print("Bạn đã chọn phim thể loại Khoa học viễn tưởng.")
else:
    print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5.")