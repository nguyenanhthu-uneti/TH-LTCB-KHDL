so = int(input("Nhap so co ba chu so: "))
if so<100 or so>999:
    print("Vui long nhap so co 3 chu so")
else:
    don_vi=["","mot","hai","ba","bon","nam","sau","bay","tam","chin"]
    tram=so//100
    chuc=(so//10)%10
    donvi=so%10
    print(don_vi[tram], "tram", end=" ")
    if chuc==0:
        if donvi!=0:
            print("le", end=" ")
    elif chuc==1:
        print("muoi", end=" ")
    else:
        print(don_vi[chuc], "muoi", end=" ")
    if chuc>1:
        if donvi==1:
            print("mot")
        elif donvi==5:
            print("lam")
        elif donvi>0:
            print(don_vi[donvi])
    elif donvi>0:
        print(don_vi[donvi])