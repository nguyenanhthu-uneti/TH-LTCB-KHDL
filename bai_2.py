x=int(input("nhap so x: "))
y=int(input("nhap so y: "))
a=int(input("nhap so a: "))
b=int(input("nhap so b: "))
R=int(input("nhap so R: "))
IM=((x-a)**2 + (y-b)**2)**0.5
print(f"ket qua la :{IM}")
if IM==R or IM<R:
    print("TRUE")
else:
    print("False")