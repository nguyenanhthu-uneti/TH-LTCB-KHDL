import math
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))

i = 0
cos_taylor = 0
while i <= n:
    term = ((-1)**i * x**(2*i)) / math.factorial(2*i)
    cos_taylor += term
    i += 1
if n > 1:
    cos_approx = 1 - x**3 / (n * (n - 1))
else:
    print("n phải lớn hơn 1 để dùng công thức gần đúng thứ 2.")
    exit()
sai_so = abs(cos_taylor - cos_approx)


print(f"Giá trị gần đúng theo Taylor: {cos_taylor}")
print(f"Giá trị gần đúng theo công thức x^3/(n(n-1)): {cos_approx}")
print(f"Sai số tuyệt đối: {sai_so}")


if sai_so < 1e-4:
    print("Sai số nhỏ hơn 10^-4 → đạt yêu cầu.")
else:
    print("Sai số lớn hơn 10^-4 → chưa đạt yêu cầu.")

# Nhập giá trị x: 1.2
# Nhập giá trị n: 2
# Giá trị gần đúng theo Taylor: 0.3664
# Giá trị gần đúng theo công thức x^3/(n(n-1)): 0.13600000000000012
# Sai số tuyệt đối: 0.23039999999999988
# Sai số lớn hơn 10^-4 → chưa đạt yêu cầu.