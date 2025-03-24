# input:Nhap vao so nguyen duong n: 234
# output:hai ba bon
so = {
    '0': 'khong', '1': 'mot', '2': 'hai', '3': 'ba', '4': 'bon',
    '5': 'nam', '6': 'sau', '7': 'bay', '8': 'tam', '9': 'chin'
}
while True:
    n = input("Nhap vao so nguyen duong n: ")
    if int(n) > 0:
        break
    print("Yeu cau nhap lai")
chu = []
for i in n:
    chu.append(so[i])  
print(' '.join(chu))