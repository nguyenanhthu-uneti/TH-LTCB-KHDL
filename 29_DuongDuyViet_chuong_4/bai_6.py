chu_so = {
    '0': 'không', '1': 'một', '2': 'hai', '3': 'ba', '4': 'bốn',
    '5': 'năm', '6': 'sáu', '7': 'bảy', '8': 'tám', '9': 'chín'
}
while True:
    n = input("Nhập vào số nguyên dương n: ")
    if int(n) > 0:
        break
    print("nhập lại")
in_chu = []
for i in n:
    in_chu.append(chu_so[i])  
print(' '.join(in_chu))
