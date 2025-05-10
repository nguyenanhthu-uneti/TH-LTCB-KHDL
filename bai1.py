print("chương trình kiểm tra một năm có phải năm nhuận hay không")
nam=int(input("nhập năm bạn muốn kiêm tra : "))
if (nam %4==0 and nam %100!=0) or (nam%400==0):
    print("năm",nam,"là năm nhuận !")
else:
    print("năm",nam,"không là năm nhuận !")
