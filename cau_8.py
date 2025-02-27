# Viết chương trình phân loại sinh viên dựa vào kết quả điểm học tập. Nếu điểm A thì
# phân loại là sinh viên xuất sắc, điểm B là sinh viên loại giỏi, điểm C là sinh viên loại
# khá, điểm D là sinh viên loại trung bình, điểm E là sinh viên loại yếu, điểm F là sinh
# viên xếp loại kém.
nhap_lua_chon = input("Nhập kết quả học sinh: ")
nhap_lua_chon = nhap_lua_chon.upper()

if nhap_lua_chon == "A":
    print("Sinh viên xuất sắc")
elif nhap_lua_chon == "B":
    print("Sinh viên loại giỏi")
elif nhap_lua_chon == "C":
    print("Sinh viên loại khá")
elif nhap_lua_chon == "D":
    print("Sinh viên loại trung bình")
elif nhap_lua_chon == "E":
    print("Sinh viên loại yếu")
elif nhap_lua_chon == "F":
    print("Sinh viên không đạt")
else:
    print("Bạn nhập sai lựa chọn của bạn")
