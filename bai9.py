luong = input("nhap so luong vao day(tr)")
if luong == 15 :
    thue = luong* (30/100)
    luong_rong = luong - thue
    print(thue)
    print(luong_rong)
elif 7 <= luong < 15:
    thue = luong* (20/100)
    luong_rong = luong - thue
    print(thue)
    print(luong_rong)
else:
    thue = luong* (10/100)
    luong_rong = luong - thue
    print(thue)
    print(luong_rong)