a,b=map(float,input('nhap toa do I : ').split())
r = float(input('moi nhap ban kinh r : '))
x,y=map(float,input('nhap to do diem M : ').split())
import math
d=math.sqrt((x-a)**2+(y-b)**2)
print(f'IM la: {d:.2f}')
if d<r:
    print('diem M nam trong duong tron')
elif d==r:
    print('diem M nam tren duong tron')
else:
    print('diem M nam ngoai duong tron')