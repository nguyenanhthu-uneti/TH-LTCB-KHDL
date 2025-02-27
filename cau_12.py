than_nien_cong_tac = float(input("Nhap tham nien cong tac: "))
luong_co_ban = 1350000
if than_nien_cong_tac < 12:
    he_so = 2.34
elif than_nien_cong_tac >= 12 and than_nien_cong_tac < 36:
    he_so = 3.33
elif than_nien_cong_tac >= 36 and than_nien_cong_tac < 60:
    he_so = 3.66
elif than_nien_cong_tac >= 60:
    he_so = 3.99
luong = he_so*luong_co_ban
print(f'Luong cua nhan vien la: {luong}')