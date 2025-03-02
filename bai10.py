thang_co_31_ngay = [1,3,5,7,8,10,12]
thang_co_30_ngay = [4,6,9,11]
thang_co_28_hoac_29_ngay = [2]
lua_chon = input("nhap thang:")
if lua_chon == 1 or lua_chon == 3 or lua_chon == 5 or lua_chon == 7 or lua_chon == 8 or lua_chon == 10 or lua_chon == 12 :
    print(f"thang {lua_chon} co 31 ngay")
elif lua_chon == 2:
    print(f"thang {lua_chon} co 28 hoac 29 ngay")
else: 
    print(f"thang{lua_chon} co 30 ngay")
