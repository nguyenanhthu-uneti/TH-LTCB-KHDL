a,b,c = map(float,input('nhập độ dài các cạnh: ').split(","))
if a+b+c or b+c<a or c+a<b:
    print('không phải là 3 cạnh của tam giác')
elif a==b or a==c or b==c:
    if a==b==c:
        print("đây là tam giác đều")
    elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
        print('đây là tam giác vuông cân')
    else:
        print('đây là tam giác cân')
elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
     print('đây là tam giác vuông')
else: print('đây là tam giác thường')