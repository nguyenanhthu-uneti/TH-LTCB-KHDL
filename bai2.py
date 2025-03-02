a = float(input("nhap hoanh do tam i"))
b = float(input("nhap tung do tam i"))
x = float(input("nhap hoanh do diem m"))
y = float(input("nhap tung do diem m"))
R = int(input("nhap ban kinh"))
im = ((x -a )**2 +(y - b)**2)**1/2
if im < R:
   print("True")
elif im == R:
    print("True")
else:
    print("False")
 