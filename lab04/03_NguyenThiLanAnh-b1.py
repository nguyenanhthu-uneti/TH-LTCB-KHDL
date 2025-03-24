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
        s4=0
        for i in range(1,n+1):
            s4+=i**2
        print(f"S4 = {s4}")
        break
# input:0 -> ouput: Yeu cau nhap dung n>0 !!
# input:5 -> ouput: S5 = 153

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
        s5=0
        for i in range(1,n+1):
            if i%2!=0:
                s5+=i**3
        print(f"S5 = {s5}")
        break
# input:0 -> ouput: Yeu cau nhap dung n>0 !!
# input:5 -> ouput: S5 = 153

#c)
while True:
    try:
        n=int(input("Nhap vao so nguyen duong n: "))
        if n<=0:
            print("Yeu cau nhap dung n>0 !!")
            continue
    except:
        print("Vui long nhap dung yeu cau !!")
    else:
        s6=0
        for i in range(1,n+1):
            if i%2==0:
                s6+=i**4
        print(f"S6 = {s6}")
        break
# input:0 -> ouput: Yeu cau nhap dung n>0 !!
# input:5 -> ouput: S6 = 272