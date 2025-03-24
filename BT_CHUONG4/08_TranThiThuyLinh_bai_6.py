#Viet chuong trinh nhap vao mot so tu ban phim va in ra man hinh bang chu
n = int(input("Nhập một số: "))
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
ket_qua = ""
while n > 0:
    ket_qua = chu_so[n % 10] + " " + ket_qua
    n //= 10
print("Kết quả:", ket_qua.strip())
#input: 2216
#output: hai hai mot sau