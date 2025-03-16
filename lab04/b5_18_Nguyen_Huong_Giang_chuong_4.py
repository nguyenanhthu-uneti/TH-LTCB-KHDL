# 5. Viết chương trình nhập vào số bất kỳ đến khi nhập số âm thì dừng lại.

while True:
    so = int(input("Nhập một số: "))
    if so < 0:
        print(" Có số âm. Dừng chương trình .")
        break

# input : Nhập một số : 3
#         Nhâp một số: -2
# output: Có số âm . Dừng chương trình