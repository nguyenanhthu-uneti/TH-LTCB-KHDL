while True:
    try:
        diem = input("Nhap diem tu A-F: ").upper()
        if diem not in ('A','B','C','D','E','F'):
            print("Yeu cau nhap diem tu A-F !!")
            continue
    except:
        print("Vui long nhap dung yeu cau !!")
    else:
        if diem == "A":
            print("Sinh vien xuat sac")
        elif diem == "B":
            print("Hoc sinh loai gioi")
        elif diem == "C":
            print("Hoc sinh loai kha")
        elif diem == "D":
            print("Hoc sinh loai trung binh")
        elif diem == "E":
            print("Hoc sinh loai yeu")
        elif diem == "F":
            print("Hoc sinh loai kem")
        else:
            print("Diem khong hop le vui long nhap")
        break