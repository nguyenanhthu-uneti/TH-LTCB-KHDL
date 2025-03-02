n = int(input ("nhap nam:"))
if n % 4 == 0 and n % 100 !=0:
    print ("day la nam nhuan")
elif n % 400 == 0:
    print("day la nam nhuan")
else:
    print("day ko phai nam nhuan")