# Viết chương trình kiểm tra một ký tự trong bảng chữ cái tiếng anh là nguyên âm hay
# phụ âm. Ký tự là bất kỳ được nhập từ bàn phím.
#Kiểm tra kí tự trong bảng chữ cái tiếng anh là nguyên âm hay phụ âm
ki_tu =str(input("Nhập một kí tự bất kì trong bảng chữ cái tiếng anh :"))
if ki_tu == "u" or ki_tu == "e" or ki_tu == "o" or ki_tu == "a" or ki_tu == "i":
    print(f'Kí tự {ki_tu} là nguyên âm')
else:
    print(f'Kí tự {ki_tu} là phụ âm')