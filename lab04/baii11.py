print("MENU")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt")
print("4. Nước lọc")
print("5. Nước dừa")
lua_chon = ""


while lua_chon not in ["1", "2", "3", "4", "5"]:  # Lặp lại nếu nhập sai
    lua_chon = input("Vui lòng chọn đồ uống (1-5): ")
    if lua_chon not in ["1", "2", "3", "4", "5"]:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại!")


if lua_chon == "1":
    do_uong = "Cafe"
elif lua_chon == "2":
    do_uong = "Cam vắt"
elif lua_chon == "3":
    do_uong = "Nước ép cà rốt"
elif lua_chon == "4":
    do_uong = "Nước lọc"
else:
    do_uong = "Nước dừa"


print(f"Bạn đã chọn: {do_uong}")

# MENU
# 1. Cafe
# 2. Cam vắt
# 3. Nước ép cà rốt
# 4. Nước lọc
# 5. Nước dừa
# Vui lòng chọn đồ uống (1-5): 6
# Lựa chọn không hợp lệ, vui lòng chọn lại!
# Vui lòng chọn đồ uống (1-5): 5
# Bạn đã chọn: Nước dừa

