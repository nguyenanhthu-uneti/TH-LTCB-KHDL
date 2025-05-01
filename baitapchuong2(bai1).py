nam = int(input("nhập nam: "))
if nam % 4 ==0 and nam % 100 !=0:
 print(f"{nam}là năm nhuận")
elif nam % 400 == 0:
 print(f"{nam} là namư nhuận")
else:
 print(f"{nam} không phải là năm nhuận")
