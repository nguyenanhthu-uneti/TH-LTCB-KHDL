#Viet chuong trinh nhap vao tu so va mau so cua mot phan so, kiem tra mau so nhap la so 0 thi nhap lai
tu_so = int(input("Nhap tu so: "))
mau_so = int(input("Nhap mau so: "))
while mau_so == 0:
    print("Yeu cau nhap lai mau so khac 0")
    break
print(tu_so/mau_so)
#input
#tu so = 2
#mau so = 3
#output = 2/3

    
