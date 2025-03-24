# input:Nhap vao so thap phan n: 3.55
# output:3.55 la ba phay nam nam
so = {
    '0': 'khong', '1': 'mot', '2': 'hai', '3': 'ba', '4': 'bon',
    '5': 'nam', '6': 'sau', '7': 'bay', '8': 'tam', '9': 'chin','.':'phay'
}
while True:
    n = input("Nhap vao so thap phan n: ")
    chu = []
    for i in n:
        chu.append(so[i])  
    print(f"{n} la",' '.join(chu))