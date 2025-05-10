so = input("Nhập một số thập phân: ")
chu_so = {
    '0': "khong", '1': "mot", '2': "hai", '3': "ba", '4': "bon",
    '5': "nam", '6': "sau", '7': "bay", '8': "tam", '9': "chin"}
i = 0
ket_qua = ""
while True:
    try:
        ky_tu = so[i]
        if ky_tu == '.':
            ket_qua += "chấm "
        else:
            ket_qua += chu_so[ky_tu] + " "
        i += 1
    except IndexError:
        break
print(ket_qua.strip())
