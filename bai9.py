# input:Nhap 1 so: 456
# output:Tong cac chu so cua so vua nhap la: 15
n = input("Nhap 1 so: ")
tong = sum(int(i) for i in n)
print(f"Tong cac chu so cua so vua nhap la: {tong}")
