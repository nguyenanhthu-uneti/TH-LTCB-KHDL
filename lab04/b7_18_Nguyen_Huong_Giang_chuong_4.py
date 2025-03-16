# 7. Viết chương trình tìm bội chung nhỏ nhất của hai số nguyên được nhập từ bàn phím.

so_1 = int(input("Nhập số nguyên thứ nhất: "))
so_2 = int(input("Nhập số nguyên thứ hai: "))

BCNN = max(so_1, so_2)  
while True:
    if BCNN % so_1 == 0 and BCNN % so_2 == 0:
        break 
    BCNN += 1  
print(f"Bội chung nhỏ nhất của {so_1} và {so_2} là: {BCNN}")

# input : Nhập số nguyên thứ nhất : 4
#         Nhập số nguyên thứ hai : 9
# Bội chung nhỏ nhất của 4 và 9 là : 36