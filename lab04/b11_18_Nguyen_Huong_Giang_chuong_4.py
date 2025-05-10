# 11. Viết chương trình gọi đồ uống. Giả sử menu của chúng ta có các loại thức uống như sau:

# 1. Cafe
# 2. Cam vắt
# 3. Nước ép cà rốt

# 4. Nước lọc
# 5. Nước dừa

print("Menu đồ uống:")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt")
print("4. Nước lọc")
print("5. Nước dừa")


lua_chon = 0
while lua_chon < 1 or lua_chon > 5:
    lua_chon = int(input("Nhập vào số tương ứng với dồ uống bạn chọn: "))
    if lua_chon < 1 or lua_chon > 5:
        print("Vui lòng chọn số từ 1 đến 5 ")

if lua_chon == 1:
    print("cafe.")
elif lua_chon == 2:
    print("cam vắt.")
elif lua_chon == 3:
    print("nước ép cà rốt.")
elif lua_chon == 4:
    print("nước lọc.")
else:
    print("nước dừa.")

# input: Nhập vào số tương ứng với dồ uống bạn chọn: 5
# output: nước dừa

