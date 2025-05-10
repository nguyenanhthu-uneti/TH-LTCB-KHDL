thang = int(input("nhap vao so thang (1-12):"))
if thang in [1,3,5,7,8,10,12]:
                  ngay = 31
elif  thang in [4,6,9,11]:
                  ngay = 30
elif thang == 2:
                  ngay = 28
else:
                  ngay = "khong hop le"
print(f"thang {thang} co {ngay} ngay ")