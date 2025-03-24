print("---MENU---")
print("1. Cafe")
print("2. Cam vat")
print("3. Nuoc ep ca rot")
print("4. Nuoc loc")
print("5. Nuoc dua")
while True:
    try:
        lua_chon=int(input("Nhap do uong muon goi(1-5): "))
        if lua_chon<=0 or lua_chon>5:
            print("Yeu cau chi lua chon do uong tu 1-5")
            continue 
    except:
        print("Vui long nhap dung lua chon")
    else:
        if lua_chon==1:
            print("Cafe")
        elif lua_chon==2:
            print("Cam vat")
        elif lua_chon==3:
            print("Nuoc ep ca rot")
        elif lua_chon==4:
            print("Nuoc loc")
        else:
            print("Nuoc dua")
        break
# ---MENU---
# 1. Cafe
# 2. Cam vat
# 3. Nuoc ep ca rot
# 4. Nuoc loc
# 5. Nuoc dua
# Nhap do uong muon goi(1-5): 6
# Yeu cau chi lua chon do uong tu 1-5
# Nhap do uong muon goi(1-5): 8
# Yeu cau chi lua chon do uong tu 1-5
# Nhap do uong muon goi(1-5): 3
# Nuoc ep ca rot