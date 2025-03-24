#input:Nhap lua chon: 4
    #Nhap so luong: 2
#output:Da goi 2 Nuoc loc
#input:Nhap lua chon:6
#output:Da goi mon xong
while True:
    print('---MENU---')
    print("1.Cafe")
    print("2.Cam vat")
    print("3.Nuoc ep ca rot")
    print("4.Nuoc loc")
    print("5.Nuoc dua")   
    print("6.Da chon xong")  
    n = int(input("Nhap lua chon: "))
    if n == 1:
        a = int(input("Nhap so luong: "))
        print(f"Da goi {a} Cafe")
    elif n == 2:
        b = int(input("Nhap so luong: "))
        print(f"Da goi {b} Cam vat")
    elif n == 3:
        c = int(input("Nhap so luong: "))
        print(f"Da goi {c} Nuoc ep ca rot")
    elif n == 4:
        d = int(input("Nhap so luong: "))
        print(f"Da goi {d} Nuoc loc")
    elif n == 5:
        e = int(input("Nhap so luong: "))
        print(f"Da goi {e} Nuoc dua")
    elif n==6:
        print("Da goi mon xong")
        
        break
    