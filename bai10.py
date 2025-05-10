
n = int(input("Nhập tháng cần kiểm tra: "))
m = int(input("Nhập năm cần kiểm tra: "))
if n >= 1 and n <= 12 and m > 0:
    if n == 1 or n == 3 or n == 5 or n ==7 or n == 8 or n == 10 or n == 12: 
        print(f'Thang {n} co 31 ngay')
    elif n == 4 or n == 6 or n == 9 or n == 11:
        print(f'Thang {n} co 30 ngay')
    elif n == 2:
        if m % 4 == 0 and m % 100 != 0 or m % 400 == 0:
            print(f'{m } la nam nhuan, va thang {n} co 29 ngay')
        else:
            print(f'Thang {n} co 28 ngay')
else:
    print("Yêu cầu nhập lại tháng ")
  