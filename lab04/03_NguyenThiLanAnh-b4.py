while True:
    try:
        tu=int(input("Nhap vao tu so: "))
        mau=int(input("Nhap vao mau so: "))
        if mau==0:
            print("Yeu cau nhap mau so !=0 !!")
            continue
    except:
        print("Vui long nhap dung yeu cau")
    else:
        print(f"Phan so la: {tu}/{mau}")
        break
# Nhap vao tu so: 4
# Nhap vao mau so: 5
# Phan so la: 4/5