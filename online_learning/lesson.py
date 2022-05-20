'''
print("a")
#print("b")
#print("c")
'''
##import turtle t=turtle.Pen()
##for x in range(360):
##    t.forward(x)
##    t.left(59)


##turtle模块练习
##import turtle         #导入turtle模块   
##turtle.showturtle()    #显示箭头
##turtle.write("bowen")  #写字符串
##turtle.forward(300)    #前进300像素
##turtle.color("red")    #画笔颜色改为红色
##turtle.left(90)        #箭头左转90度
##turtle.forward(300)    
##turtle.goto(0,50)      #去坐标（0，50）
##turtle.goto(0,0)
##turtle.penup()        #抬笔，路径不会画出来
##turtle.goto(0,300)
##turtle.pendown()      #下笔，路径画出来
##turtle.circle(100)   #画圆



##奥运五环
import turtle

turtle.width(10)

turtle.color("blue")
turtle.circle(50)

turtle.penup()
turtle.goto(120,0)
turtle.pendown()

turtle.color("black")
turtle.circle(50)

turtle.penup()
turtle.goto(240,0)
turtle.pendown()

turtle.color("red")
turtle.circle(50)

turtle.penup()
turtle.goto(60,-50)
turtle.pendown()

turtle.color("yellow")
turtle.circle(50)

turtle.penup()
turtle.goto(180,-50)
turtle.pendown()

turtle.color("green")
turtle.circle(50)
