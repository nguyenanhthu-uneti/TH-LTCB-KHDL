import math

def cos_taylor(x, epsilon=1e-4):
    term = 1
    cos_x = term
    n = 1
    
    while abs(term) > epsilon:
        term *= -x**2 / ((2*n - 1) * (2*n))
        cos_x += term
        n += 1
    
    return cos_x

x = float(input("Nhập giá trị x (radian): "))
result = cos_taylor(x)
print(f"Giá trị gần đúng của cos({x}) là: {result}")
print(f"Giá trị thực tế của cos({x}) từ math.cos: {math.cos(x)}")


# Nhập giá trị x (radian): 0.5
# Giá trị gần đúng của cos(0.5) là: 0.8775824652777777
# Giá trị thực tế của cos(0.5) từ math.cos: 0.8775825618903728