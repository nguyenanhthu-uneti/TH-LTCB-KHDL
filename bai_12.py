tnct=int(input("Nhập số thâm niên công tác: "))
luongcb=1350000
if tnct<12:
    luong=2.34*luongcb
    print(f"Lương của bạn là: {luong}")
elif tnct>=12 or tnct<36:
    luong=3.33*luongcb
    print(f"Lương của bạn là: {luong}")
elif tnct>=36 or tnct<60:
    luong=3.66*luongcb
    print(f"Lương của bạn là: {luong}")
elif tnct>=60:
    luong=3.99*luongcb
    print(f"Lương của bạn là: {luong}")
