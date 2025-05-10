a = float(input("nhap canh a:"))
b = float(input("nhap canh b:"))
c = float(input("nhap canh c:"))
if a + b <= c or a + c <= b or b + c <= a:
                  print(" day khong phai bo ba canh tam giac")
else:
                  if a == b == c:
                                    print("day la tam giac deu")
                  elif a == b or b == c or a == c:
                                    print("day la tam giac can")
                  elif (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
                                    print("day la tam giac vuong")
                  elif (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2) and (a == b or b == c or a == c):
                                    print("day la tam giac vuong can")
                  else:
                                    print("day la tam giac thuong")
                                    
                                    