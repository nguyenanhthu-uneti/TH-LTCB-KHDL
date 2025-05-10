chu_so = ["khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]
n = input("Nhap mot so vao n: ")
i = 0
result = ""
while i < len(n):
    result += chu_so[int(n[i])] + " "
    i += 1
print(result.strip())
# Nhap mot so vao n: 123
# mot hai ba