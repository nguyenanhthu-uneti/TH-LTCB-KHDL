# Viết chương trình nhập vào tử số và mẫu số của một phân số, kiểm tra mẫu số nhập
# là số 0 thì nhập lại.
tu_so = int(input("Nhap tu so cua ban la :"))
mau_so = int(input("Nhap mau so cua ban la :"))
while mau_so == 0 :
    mau_so = int(input("Nhap tu so khng được bằng 0 : "))
print(tu_so/mau_so)
#input
# Nhap tu so cua ban la :2
# Nhap mau so cua ban la :3
# output
# 0.6666666666666666
