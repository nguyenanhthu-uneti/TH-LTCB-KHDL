while True:
    try:
        so=int(input("Nhap so: "))
        if so>0:
            print("Nhap tiep den khi nhap so am")
            continue
    except:
        print("Yeu cau chi nhap so")
    else:
        print("Stop")
        break
# Nhap so: 1
# Nhap tiep den khi nhap so am
# Nhap so: 2
# Nhap tiep den khi nhap so am
# Nhap so: -4
# Stop