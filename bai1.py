n = int(input("nhap so nam vao day"))
if n % 4 ==0 and n % 100 !=0:
    print("day la nam nhuan")
elif n % 400 ==0:
    print("day la nam nhuan")
else:
    print("day khong phai la nam nhuan")
