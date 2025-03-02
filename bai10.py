n = int(input("nhap thang vao day"))
if n == 2:
    k = int(input("nhap nam vao day"))
    if k %4 ==0 and k % 100 !=0:
        print("la nam nhuan nen thang 2 co 29")
    elif k % 400==0:
        print("la nam nhuan nen thang 2 co 29")
    else:
        print("khong phai nam nhuan nen thang 2 co 28 ngay")
elif n ==1 or n == 3 or n == 5 or n == 7 or n ==8 or n== 10 or n ==12:
    print("thang co 31 ngay")
elif n ==4 or n ==6 or n==9 or n==11:
    print("thang co 30 ngay")
else:
    print("nhap lai thang")
    