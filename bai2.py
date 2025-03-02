a,b=map(float,input('nhập tọa độ tâm I : ').split())
r = float(input('mời nhập bán kính r : '))
x,y=map(float,input('nhập tọa độ điểm M : ').split())
import math
d=math.sqrt((x-a)**2+(y-b)**2)
print(f'IM la: {d:.2f}')
if d<r:
    print('điểm M nằm trong đường tròn ')
elif d==r:
    print('điểm M nằm trên đường tròn ')
else:
    print('điểm M nằm ngoài đường tròn ')