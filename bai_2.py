x = float(input("nhập toa độ x của điểm M:"))
y = float(input("nhập toa độ y của điểm M:"))
a = float(input("nhập toa độ a của điểm I:"))
b = float(input("nhập toa độ b của điểm I:"))
R = float(input("nhập bán kính R của đường tròn:"))
IM = ((x - a) ** 2 + (y - b) ** 2) ** 0.5
print("Khoảng cách từ điểm M đến điểm I là:", IM)
if IM < R:
    print("Điểm M nằm trong đường tròn")
elif IM == R:
    print("Điểm M nằm trên đường tròn")
else:
    print("Điểm M nằm ngoài đường tròn")