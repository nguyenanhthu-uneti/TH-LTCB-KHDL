n = int(input(" Nhap vao năm nhuan n: "))
if n % 4 == 0 and n % 100 != 0:
    print(" Day la nam nhuan ")
elif n % 400 == 0 :
    print(" Day la nam nhuan ")
else:
    print(" Day khong la nam nhuan ")
    