x= float(input("nhap vao x:"))
y= float(input("nhap vao y:"))
a= float(input("nhap vao a:"))
b= float(input("nhap vao b:"))
R= float(input("nhap vao R:"))
do_dai = (((x-a)**2+(y-b)**2)**1/2)
print("do dai IH:(do_dai)")
if do_dai <= R:
    print("true")
else:
    print("flase")


