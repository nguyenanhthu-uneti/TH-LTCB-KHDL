thang = int(input("Nhap so thang (1-12): "))
if thang in [1,3,5,7,8,10,12]:
    print(f"Thang nay {thang} co 31 ngay")
elif thang in [4,6,9,11]:
    print(f"Thang nay {thang} co 30 ngay")
elif thang == 2:
    print(f"Thang nay {thang} co 28 hoac 29 ngay")
else:
    print("lua chon khong hop le vui long nhap lai")