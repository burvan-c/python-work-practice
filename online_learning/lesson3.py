##字符串不可改变，不支持单字符类型。单引号或双引号。
##三个单引号或双引号创建多行字符串
a="abc"
print(a)
resume='''name="陈博文"
school="合工大"
age=24
lover="编程"'''
print(resume)



##字符串拼接
print('aa'+'bb')
print('aa''bb')



##字符串的复制
print('aa'*4)

##一般情况打印后自动换行，end=''--可以不换行
print('aa',end='*')


##使用input()从控制台读取输入内容

##str()将其他类型转为字符串

##使用[]提取字符串中的字符，[]内为正--从左向右提取，为负则相反

##replace替换字符


# print函数可以是数字、字符串、表达式
print('\n',3+1)    #不同类型要用英文逗号隔开


#将数据输入到文件
fp=open('D:/text.txt','a+')   #D盘新建文件text.txt并赋给变量fp   a+:若文件不存在直接创建，若文件存在直接追加内容
print('helloworld',file=fp)   #在文件中打印helloworld
fp.close()                    #注意：所指盘必须存在，使用file=的形式



#不换行输出
print('hello','world','python')     #a+:若文件不存在直接创建，若文件存在直接追加内容



#转义字符
print('hello\nworld')#\n--换行
print('hello\tworld')#\t--tab制表符
print('hello\rworld')#\r--回车
print('hello\bworld')#\b--退格
print('http:\\\\www.baidu.com')#\\--输出为一个\
print('老师说:\'大家好\'')#\'--输出单引号


#原字符，使转义字符不起作用，在字符前加r或R,最后一个字符不可以是\
print(r'hello\tworld')


name='玛丽亚'
print('标识',id(name))
print('类型',type(name))
print('值',name)

