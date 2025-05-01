
ky_tu = input("Nhập một ký tự: ")


if len(ky_tu) == 1:
    ascii_value = ord(ky_tu)  
    print(f"Giá trị ASCII của '{ky_tu}' là {ascii_value}")
else:
    print("Vui lòng nhập một ký tự duy nhất.")


# Nhập một ký tự: H
# Giá trị ASCII của 'H' là 72