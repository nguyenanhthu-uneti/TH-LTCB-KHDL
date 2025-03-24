n = int(input("Nhap so nguyen duong n can kiem tra: "))
while n < 0:
    print("Yeu cau nhap lai so nguyen duong")
S1 = 0
k = 0
while k <= n:
    S1 += (-1)**k/(k+1)
    k += 1
S2 = 0
i = 1
while i <= n:
    S2 += 1/i*(i+1)
    i += 1
S3 = 0
h = 2
while h <= n:
    S3 += 1/(h+1)**0.5
    h += 1    
print(S1)
print(S2)
print(S1)
#input = 3
#output:
#S1 = 0,83333333333
#S2 = 0,75
#S3 = 1,7844




    