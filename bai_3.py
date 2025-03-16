a=float(input("nhap so a: "))
b=float(input("nhap so b: "))
c=float(input("nhap so c: "))
if (a<=0 and b<=0 and c<=0) and (a+b<=c or a+c<=b or b+c<=a):
    print(" ko là cạnh tam giác")
elif a**2 + b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
    print("tam giác vuông")
elif (a**2 + b**2==c**2 and a==b) or (a**2+c**2==b**2 and a==c) or (b**2+c**2==a**2 and b==c): 
    print("tam giác vuông cân")
elif a==b!=c or a==c!=b or b==c!=a:
    print("tam giác cân")
elif a==b==c:
    print("tam giác đều")
else :
    print("là tam giác thương")