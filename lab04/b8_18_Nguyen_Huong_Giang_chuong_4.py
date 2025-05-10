# 8. Viết chương trình tìm giá trị ASCII của một ký tự bất kỳ được nhập từ bàn phím.


ky_tu = input("Nhập một ký tự: ")

while len(ky_tu) != 1:
    print("Vui lòng chỉ nhập một ký tự!")
    ky_tu = input("Nhập một ký tự: ")

ascii_value = ord(ky_tu)

print(f"Giá trị ASCII của '{ky_tu}' là: {ascii_value}")

# input : Nhập một kí tự: k
# Giá trị ASCII của "k" là : 107