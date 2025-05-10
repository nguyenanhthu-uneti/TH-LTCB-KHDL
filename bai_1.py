n = int(input("nhập n:"))
if n % 4 == 0 and n % 100 != 0:
                  print("đây là nam nhuận")
elif n % 400 == 0:
                  print("đay là năm nhuận")
else:
                  print("đay không phải năm nhuận")
                        