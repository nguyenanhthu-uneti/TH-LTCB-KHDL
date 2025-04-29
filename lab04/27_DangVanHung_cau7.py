so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))

lon_hon = max(so1, so2)

while True:
    if lon_hon % so1 == 0 and lon_hon % so2 == 0:
        bcnn = lon_hon
        break
    lon_hon += 1

print("BCNN của", so1, "và", so2, "là:", bcnn)
