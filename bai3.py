a = float(input(" nhap gia tri a:"))
b = float(input(" nhap gia tri b:"))
c = float(input(" nhap gia tri c:"))
if (a+b <=c) or (a+c <=b) or (b+c <=a):
    print("ko phai 3 canh tm giac")
elif a == b == c:
    print ("tam giac deu")
elif a==b or b==c or c==a:
    print("tam giac can")
elif a**2 + b**2:
    print ("tam giac vuong")
else:
    print("tam giac thuong")