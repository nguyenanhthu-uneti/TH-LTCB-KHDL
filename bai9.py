luong = float(input("nhap vao luong:"))
if luong < 7:
    luong_rong = luong - (luong * (10/100))
    print(f"Tien luong cua ban la {luong_rong}")
elif luong >= 7 and luong <= 15 :      
    luong_rong = luong - (luong * (20/100))
    print(f"Tien luong cua ban la {luong_rong}")
elif luong > 15 :
    luong_rong = luong - (luong * (30/100))
    print(f"Tien luong cua ban la {luong_rong}")



    