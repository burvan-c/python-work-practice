# 学习对象：python
# 学习人员：陈博文
# 学习目标：入门-->精通
#input(str)函数     变量=input()
present=input('大圣想要什么礼物？')#运行后要先输入，按回车键，这之后才能继续运行
print(present,type(present))



#input高级运用
a=input('请输入一个加数:')
b=input('请输入另一个加数:')
print(a+b)#input参数是str类型----'1'+'2'='12'这里输出的是字符串
print(int(a)+int(b))#转换类型后输出数字3