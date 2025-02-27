ten=input("Nhap ten sv: ")
while True:
    diem=input("Nhap diem sv: ")
    if diem=='A':
        print(f"SInh vien {ten} la sinh vien xuat sac")
        break
    elif diem=='B':
        print(f"Sinh vien {ten} la sinh vien gioi")
        break
    elif diem=='C':
        print(f"Sinh vien {ten} la sinh vien kha")
        break
    elif diem=='D':
        print(f"Sinh vien {ten} la sinh vien trung binh")
        break
    elif diem=='F':
        print(f"Sinh vien {ten} la sinh vien yeu")
        break
    else:
        print("Nhap lai diem")