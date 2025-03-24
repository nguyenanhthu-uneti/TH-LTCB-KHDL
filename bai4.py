a = int(input("Nhap tu so: "))
b = int(input("Nhap mau so: "))
while b == 0:
    c = int(input("Yeu cau nhap lai mau so: "))
    print(f"phan so la:{a}/{c}")
    break
else:
    print(f"Phan so la:{a}/{b}") 
# input:Nhap tu so: 3
    #   Nhap mau so: 0
    #   Yeu cau nhap lai mau so: 5
# output:phan so la:3/5