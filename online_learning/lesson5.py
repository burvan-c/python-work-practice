# 学习对象：python
# 学习人员：陈博文
# 学习目标：入门-->精通
#测试对象的布尔值
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))#空字符串
print(bool([]))#空列表
print(bool(list()))#空列表
print(bool(()))#空元组
print(bool(tuple()))#空元组
print(bool({}))#空字典
print(bool(dict()))#空字典
print(bool(set()))#空集合
#除了以上，其他对象的布尔值都是True



money=1000#余额
s=int(input('输入取款金额 '))#取款金额
#判断余额是否充足
if money>=s:
    money=money-s
    print('取款成功，余额为:',money)
else:
    print('余额不足')



#从键盘录入一个整数，判断奇数或偶数
num=int(input('输入一个整数:'))
if 0==num%2:
    print(num,'是偶数')
else:
    print(num,'是奇数')




'''从键盘录入整数 成绩
    90-100  A
    80-89   B
    70-79   C
    60-69   D
    0-59    E
    小于0或大于100 为非法数据（不是成绩的有效范围）'''
score = int(input('输入成绩:'))
 # 判断
if 90 <= score <= 100:  # python语言独特写法，其他语言不可以这么写
    print('A级')
elif 80 <= score <= 89:
    print('B级')
elif 70 <= score <= 79:
    print('C级')
elif 60 <= score <= 69:
    print('D级')
elif 0 <= score <= 59:
    print('E级')
else:
    print('不是成绩有效范围')


    '''嵌套分支语句    会员>=200   8折
   >=100  9折
     以下     不打折 
     非会员    >=200   9.5折
    以下   不打折'''
answer = input('是否会员？y/n')
money=float(input('输入购物金额:'))
# 外层判断是否是会员
if answer == 'y':
    if money>=200:
        print('付款金额:',money*0.8)
    elif money>=100:
        print('付款金额:',money*0.9)
    else:
        print('付款金额:',money)
else:
    if money>=200:
        print('付款金额:',money*0.95)
    else:
        print('付款金额:',money)




'''从键盘录入两个整数，比较大小'''
num_a=int(input('输入第一个整数 '))
num_b=int(input('输入第二个整数 '))
#比较大小
'''if num_a>=num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)'''

print('使用条件表达式比较大小')######################################
print(str(num_a)+'大于等于'+str(num_b) if num_a>=num_b else str(num_a)+'小于'+str(num_b))######################