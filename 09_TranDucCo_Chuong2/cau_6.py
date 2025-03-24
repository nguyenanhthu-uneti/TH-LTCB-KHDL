# Viết chương trình thể hiện menu lựa chọn gồm các thể loại phim hiện đang có trong
# rạp chiếu phim ABC. Yêu cầu người dùng nhập lựa chọn thể loại phim muốn xem.
while True :
    print("Nhap lua chon cua ban(1-4)")
    print("1. Phim tinh cam")
    print("2. Phim kkinh di")
    print("3. Phim hoat hinh")
    print("4. Phim khoa hoc vien tuong")
    n = int(input("Nhập thứ tự phim bạn muốn xem:"))
    if n == 1:
        print("Bạn đã chọn phim tình cảm")
    elif n == 2:
        print("Bạn đã chọn phim kinh dị")
    elif n == 3:
        print("Bạn đã chọn phim hoạt hình")
    elif n == 4:
        print("Bạn đã chọn phim khoa học viễn tưởng")
    else:
        print("Hãy chọn lại phim")
        break