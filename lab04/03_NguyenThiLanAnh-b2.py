#a)
while True:
    try:
        n=int(input("Nhap vao so nguyen duong n: "))
        if n<=0:
            print("Yeu cau nhap dung n>0 !!")
            continue
    except:
        print("Vui long nhap dung yeu cau !!")
    else:
        s1=0
        s2=0
        for i in range(1,n+1):
            if i%2==0:
                s1-=1/i
            else:
                s2+=1/i
            s=s1+s2
        print(f"S = {s}")
        break
# Nhap vao so nguyen duong n: 3
# S = 0.8333333333333333

#b)
while True:
    try:
        n=int(input("Nhap vao so nguyen duong n: "))
        if n<=0:
            print("Yeu cau nhap dung n>0 !!")
            continue
    except:
        print("Vui long nhap dung yeu cau !!")
    else:
        s=0
        for i in range(1,n+1):
            s+=1/(i*(i+1))
        print(f"S = {s}")
        break
# Nhap vao so nguyen duong n: 4
# S = 0.8

#c)
import math
while True:
    try:
        n=int(input("Nhap vao so nguyen duong n: "))
        if n<=0:
            print("Yeu cau nhap dung n>0 !!")
            continue
    except:
        print("Vui long nhap dung yeu cau !!")
    else:
        s=0
        for i in range(2,n+1):
            s+=1/math.sqrt(i)
        print(f"S = {s}")
        break
# Nhap vao so nguyen duong n: 5
# S = 2.231670645876131