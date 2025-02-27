luong=float(input("Nhap luong: "))
if luong>=15:
    thue_thu_nhap=luong*0.3
    luong_rong=luong-thue_thu_nhap
    print(f"Thue thu nhap la: {thue_thu_nhap} trieu")
    print(f"Luong rong la: {luong_rong} trieu")
elif luong>=7 or luong<15:
    thue_thu_nhap=luong*0.2
    luong_rong=luong-thue_thu_nhap
    print(f"Thue thu nhap la: {thue_thu_nhap} trieu")
    print(f"Luong rong la: {luong_rong} trieu")
elif luong<7:
    thue_thu_nhap=luong*0.1
    luong_rong=luong-thue_thu_nhap
    print(f"Thue thu nhap la: {thue_thu_nhap} trieu")
    print(f"Luong rong la: {luong_rong} trieu")