
# n=int(input("nhap so n"))
# if (n%4==0 and n%100!=0 ) or (n%400==0):
#     print("là năm nhuận")
# else:
#     print(" ko là năm nhuận")  


# x=int(input("nhap so x"))
# y=int(input("nhap so y"))
# a=int(input("nhap so a"))
# b=int(input("nhap so b"))
# R=int(input("nhap so R"))
# IM=((x-a)**2 + (y-b)**2)**0.5
# print(f"ket qua la :{IM}")
# if IM==R or IM<R:
#     print("TRUE")
# else:
#     print("False")

# a=float(input("nhap so a"))
# b=float(input("nhap so b"))
# c=float(input("nhap so c"))
# if (a<=0 and b<=0 and c<=0) and (a+b<=c or a+c<=b or b+c<=a):
#     print(" ko là cạnh tam giác")
# elif a**2 + b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
#     print("tam giác vuông")
# elif (a**2 + b**2==c**2 and a==b) or (a**2+c**2==b**2 and a==c) or (b**2+c**2==a**2 and b==c): 
#     print("tam giác vuông cân")
# elif a==b!=c or a==c!=b or b==c!=a:
#     print("tam giác cân")
# elif a==b==c:
#     print("tam giác đều")
# else :
#     print("là tam giác thương")


# a=int(input("nhap so a"))
# b=int(input("nhap so b"))
# c=int(input("nhap so c"))
# if a>b and a>c:
#     print(" số lớn nhất là a")
# elif b>a and b>c:
#     print("số lớn nhất là b")
# else:
#     print(" số lớn nhất là c")


# a=input("nhap ký tự")
# a=a.lower()
# nguyen_am="ueoai"
# if a in nguyen_am:
#     print(f"{a} là nguyên âm")
# elif a.isalpha():
#     print(f"{a} là phụ âm")
# else:
#     print("nhập sai")



# print("Menu phim")
# print("1) phim tình cảm")
# print("2) phim hành động")
# print("3) phim hoạt hình")
# n=int(input("Nhập lựa chọn"))
# if n==1:
#     print("chọn thành công phim tình cảm")
# elif n==2:
#     print("chọn thành công phim hành động")
# elif n==3:
#     print(" chọn thành công phim hoạt hình")
# else:
#     print("nhập sai")


# n=input("nhập vào điểm").upper()
# if n=="A":
#     print("sinh viên suất sắc")
# elif n=="B":
#     print(" sinh viên loại giỏi")
# elif n=="C":
#     print("sinh viên loại khó")
# elif n=="D":
#     print("sinh viên loại trung bình")
# elif n=="E":
#     print("sinh viên loại yếu")
# elif n=="F":
#     print("sinh viên loại kém")
# else:
#     print("nhập sai")


# n=int(input("nhập vào số lương"))
# if n==15000000:
#     thue=0.3
# elif n>=7000000:
#     thue=0.2
# else:
#     thue=0.1
# thue_thu_nhap=n*thue
# luong_rong=n-thue_thu_nhap
# print(f"thuế thu nhập là:{thue_thu_nhap}")
# print(f"lương ròng là:{luong_rong}")


# n=input("nhập vào tháng")
# if n==1:
#     print("tháng 1 có 31 ngày")
# elif n==2:
#     print("tháng 2 có 28 ngày")
# elif n==3:
#     print("tháng 3 có 31 ngày")
# elif n==4:
#     print("tháng 4 có 30 ngày")
# elif n==5:
#     print("tháng 5 có 31 ngày")
# elif n==6:
#     print("tháng 6 có 30 ngày")
# elif n==7:
#     print("tháng 7 có 31 ngày")
# elif n==8:
#     print("tháng 8 có 31 ngày")
# elif n==9:
#     print("tháng 9 có 30 ngày")
# elif n==10:
#     print("tháng 10 có 31 ngày")
# elif n==11:
#     print("tháng 11 có 30 ngày")
# elif n==12:
#     print("tháng 12 có 31 ngày")
# else:
#     print("nhập sai")


# def doc_so_3_chu_so(n):
#     hang_tram = ["", "Một trăm", "Hai trăm", "Ba trăm", "Bốn trăm", "Năm trăm",
#                  "Sáu trăm", "Bảy trăm", "Tám trăm", "Chín trăm"]
#     hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi",
#                  "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
#     hang_dv = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

#     t, c, d = n // 100, (n // 10) % 10, n % 10
#     print(f"{hang_tram[t]} {'lẻ' if c == 0 and d else hang_chuc[c]} {'lăm' if d == 5 and c else hang_dv[d]}".strip())

# n = int(input("Nhập số nguyên có 3 chữ số: "))
# doc_so_3_chu_so(n)


tnct=int(input("nhập thâm niên công tác"))
luong_co_ban=1350000
if tnct<12:
    he_so=2.34
elif 12<= tnct<36:
    he_so=3.33
elif 36<= tnct <60:
    he_so=3.36
else:
    he_so=3.99
luong=he_so*luong_co_ban
print(f"lương của nhân viên là : {luong}")