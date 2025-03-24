n = int(input("Nhap so nguyen duong n: "))
S4 = 0
S5 = 0
S6 = 0
i = 1
while n <= 0:
    print("Yeu cau nhap lai so nguyen duong")
while i <= n:
    S4 += i**2
    S6 += (2*i)**4
    i += 1
print(S4)
print(S6)
k = 0
while k <= n:
    S5 += (2*k+1)**3
    k += 1
print(S5)
#input = 5
#output:
#S4 = 55
#S5 = 2556
#S6 = 15664


    
    
    
    
    