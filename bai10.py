thang = int(input('nhập vào một tháng(1-12):'))
if thang ==1 or thang ==3 or thang ==5 or thang ==7 or thang==8 or thang==10 or thang==12:
    print("tháng",thang,"có 31 ngày.")
if thang==4 or thang==6 or thang==9 or thang==11:
    print("tháng",thang,"có 30 ngày.")
if thang==2:
    print("chương trình kiểm tra năm có phải năm nhuận không")
    nam=int(input("nhập năm cần kiểm tra:"))
    if (nam %4==0 and nam   %100 !=0) or (nam%400==0):
        print("tháng",thang,"có 29 ngày")
    else:
        print("tháng",thang,"có 28 ngày.")