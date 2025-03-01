so = int(input("Nhập vào số nguyên có 3 chữ số: "))
chu_so = ("không","một","hai","ba","bốn","năm","sáu","bảy","tám","chín")
tram = so // 100
chuc = (so//10)%10
don_vi = so % 10
if 100 <= so <= 999 :
    print(chu_so[tram],"trăm",end=" ")
    if chuc == 0 and don_vi == 0 :
        print()
    elif chuc == 0 :
        print("lẻ",chu_so[don_vi])
    elif chuc == 1:
        if don_vi == 0:
            print("mười")
        elif don_vi == 5:
            print("mười lăm")
        else:
            print("mười",chu_so[don_vi])
    else:
        if don_vi == 0:
            print(chu_so[chuc],"mươi")
        elif don_vi == 1:
            print(chu_so[chuc],"mươi mốt")
        elif don_vi == 5:
            print(chu_so[chuc],"mươi lăm")
        else:
            print(chu_so[chuc],"mươi",chu_so[don_vi])
else:
    print("Chữ số không hợp lệ!")

