diem_hoc_tap=input("Nhập điểm học tập của sinh viên (A,B,C,D,E,F): ").upper()
if diem_hoc_tap == "A":
    print("Sinh viên loại Xuất sắc")
elif diem_hoc_tap == "B":
    print("Sinh viên loại Giỏi")
elif diem_hoc_tap == "C":
    print("Sinh viên loại Khá")
elif diem_hoc_tap == "D":
    print("Sinh viên loại Trung bình")
elif diem_hoc_tap == "E":
    print("Sinh viên loại Yếu")
elif diem_hoc_tap == "F":
    print("Sinh viên loại Kém")
else:
    print("Nhập sai")