# 学习对象：python
# 学习人员：陈博文
# 学习目标：入门-->精通
#input(str)函数     变量=input()
# present=input('大圣想要什么礼物？')#运行后要先输入，按回车键，这之后才能继续运行
# print(present,type(present))
#
#
#
# #input高级运用
# a=input('请输入一个加数:')
# b=input('请输入另一个加数:')
# print(a+b)#input参数是str类型----'1'+'2'='12'这里输出的是字符串
# print(int(a)+int(b))#转换类型后输出数字3




#算术运算符---加减乘除、整除、取余、幂
print(1+2)
print(1-2)
print(1*2)
print(1/2)
print(11//2)#整除运算（一正一负向下取整）
print(11%2)#一正一负取余 公式 余数=被除数-除数*商
print(2**2)

print(-11//2)
print(-11%2)

#链式赋值
a=b=c=15      #内存地址相同
print(a,id(a))
print(b,id(b))
print(c,id(c))


#参数赋值
a+=30
print(a)

#系列解包赋值
a,b,c=10,20,30
print(a,b,c)

#交换值
a,b=b,a
print(a,b)

#比较运算符
print('a>b吗？',a>b)

a=10
b=10
print(a==b)#True    a、b值相等
print(a is b)#True   a、b标识相同

lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)
print(lst1 is lst2)
print(id(lst1))
print(id(lst2))

print(a is not b)
print(lst1 is not lst2)


#布尔运算符   and(和）   or（或）   not（非）   in（包含）   not in（不包含）
a,b=1,2
print(a==1 and b==2)
print(a==1 and b<2)
print(a!=1 and b==2)
print(a!=1 and b!=2)


print(a==1 or b==2)
print(a==1 or b<2)
print(a!=1 or b==2)
print(a!=1 or b!=2)

print(not True)


s='helloworld'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)



#位运算
print(4&8)#按照二进制数每一位进行与运算，得到二进制数转为十进制即为0
print(4|8)#按照二进制数每一位进行或运算，得到二进制数转为十进制即为12

#<<左移位运算符：按照二进制高位溢出舍弃，低位补0(相当于乘以2）
print(4<<1)#向左移动一位
#>>右移位运算符：按照二进制低位溢出舍弃，高位补0（相当于除以2）
print(4>>1)#向右移动一位



#运算符优先等级
#幂 > 乘除取整取余 > 加减 > 左移位右移位 > 与 > 或 > 比较运算符 > and > or > =（有括号时先计算括号）
#算术运算符 > 位运算 > 比较运算符 > 布尔运算符 > 赋值运算符（没有括号情况下）