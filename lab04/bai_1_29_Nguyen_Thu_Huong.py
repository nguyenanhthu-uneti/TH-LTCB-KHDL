n = int(input("Nhap so n la : "))
while n <= 0 :
    n = int(input("Nhap so n la so nguyen duong  : "))
s4 = 0 
i = 1 
while i <= n :
    s4 = s4 + i ** 2 
    i =  i + 1 
print(s4)
s5 = 0 
i = 1 
while i <= (2*n - 1 ):
    s5 = s5 + i ** 3 
    i = i + 2 
print(s5)
s6 = 0 
i = 2 
while i <= (n*2) :
    s6 = s6 + i ** 4 
    i = i + 2 
print(s6)
# input :Nhap so n la : 3
# output
        # 14
        # 153
        # 1568