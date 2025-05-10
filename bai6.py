('\n\n\t\t==============MENU=============')
print("1.phim tình cảm")
print("2.phim kinh dị")
print("3.phim hoạt hình")
print("4.phim khoa học viễn tưởng")
print('\n\t\t==============END============')
#người dùng nhập lựa chọn 
print('hãy nhập lựa chọn của bạn(1-->4):',end='')
luachon=int(input())
#cấu trúc if elif else
if luachon==1:
    print('bạn đã lựa chọn thể loại phim tình cảm\n')
elif luachon==2:
    print('bạn đã lựa chọn thể loại phim kinh dị \n')
elif luachon==3:
    print('bạn đã lựa chọn thể loại phim hoạt hình \n')
elif luachon==4:
    print('bạn đã lựa chọn thể loại phim viễn tưởng khoa học \n')
else: 
    print('lựa chọn không hợp lệ.xin vui lòng kiểm tra lại ')