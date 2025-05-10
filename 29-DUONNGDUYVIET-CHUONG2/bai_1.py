nam=int(input("nhập năm bạn muốn kiêm tra : "))
if (nam %4==0 and nam %100!=0) or (nam%400==0):
    print(f"năm {nam} là năm nhuận !")
else:
        print(f"năm {nam} khong là năm nhuận !")
