# Viết chương trình tìm giá trị ASCII của một ký tự bất kỳ được nhập từ bàn phím.
kí_tự = ""
while kí_tự == "":
    kí_tự = input("Nhập một ký tự của bạn: ")
mã_ascii = ord(kí_tự)
print("Mã ASCII của", kí_tự, "là:", mã_ascii)
# Nhập một ký tự của bạn: 2
# Mã ASCII của 2 là: 50