print("Chương trình phân loại sinh viên theo điểm học tập.")
diem = input("Nhập điểm chữ của sinh viên (A, B, C, D, E, F): ")


if diem == "A":
    print("Sinh viên xếp loại Xuất sắc.")
elif diem == "B":
    print("Sinh viên xếp loại Giỏi.")
elif diem == "C":
    print("Sinh viên xếp loại Khá.")
elif diem == "D":
    print("Sinh viên xếp loại Trung bình.")
elif diem == "E":
    print("Sinh viên xếp loại Yếu.")
elif diem == "F":
    print("Sinh viên xếp loại Kém.")
else:
    print("Lựa chọn không hợp lệ. Vui lòng nhập A, B, C, D, E hoặc F.")