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