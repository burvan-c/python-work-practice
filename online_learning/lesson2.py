##del a  删除变量

##链式赋值
x=y=123

##系列解包赋值
a,b,c=4,5,6
a,b=b,a     ##实现变量互换
print(a,b)

##字母全部大写即可看作常量，在逻辑上不可修改常量，否则带来编程麻烦

divmod(10,5)##同时得到商和余数
print(divmod(10,5))

##二进制(0b或0B开头)
print(0b101)

##八进制(0o或0O开头)
print(0o17)

##十六进制(0x或0X开头)
print(0x17)

##int()实现类型转化
print(int(3.9),"\n")
print(int(True))
print(int(False))
print(int("2345"))
##print(int("234acb"))这种形式会报错



#round()返回四舍五入的值


#time.time()获取当前时刻
import time
print(time.time())








import turtle
import math

#定义多个点的坐标
x1,y1=100,100
x2,y2=100,-100
x3,y3=-100,-100
x4,y4=-100,100


#绘制折线
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)



#计算起始点和终点的距离
distance=math.sqrt((x1-x4)**2+(y1-y4)**2)

turtle.write(distance)









