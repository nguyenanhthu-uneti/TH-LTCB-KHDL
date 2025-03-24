# input:Nhap mot ki tu: AB
# output:Yeu cau nhap 1 ki tu: A
    #    Gia tri ASCII cua 'A' la 65
n = input("Nhap mot ki tu: ")
while len(n) != 1:
    n = input("Yeu cau nhap 1 ki tu: ") 
ascii_value = ord(n)
print(f"Gia tri ASCII cua '{n}' la {ascii_value}")
