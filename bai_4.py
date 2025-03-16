a = int(input("Nhap vao so thu nhat "))
b = int(input("Nhap vao so thu hai "))
c = int(input("Nhap vao so thu ba "))
if a > b and a > c:
    print(" So lon nhat la so thu nhat ")
elif b > a  and b > c:
    print(" So lon nhat la so thu hai ")
else:
    print(" So lon nhat la so thu ba ")