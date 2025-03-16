# 4. Viết chương trình nhập vào tử số và mẫu số của một phân số, kiểm tra mẫu số nhập là số 0 thì nhập lại.
Tu = int(input("Nhập tử số: "))
Mau = int(input("Nhập mẫu số : "))
while Mau == 0:
    Mau = int(input("Nhập lại mẫu số: "))
print(f"Phân số: {Tu}/{Mau}")
# input: Nhap tu so : 3 , nhap mau so : 0
# output : Nhap lai mau so: 4
# output : 3/4