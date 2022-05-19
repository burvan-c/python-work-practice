#字符串--引号括起来（可以双引号，也可以单引号）灵活运用

#"one of python's strengths is its diverse and supportive community."
#"the language 'python' is named after monty python,not the snake."

#name="ada lovelace"
#print(name.title())
##.title()--对变量name执行方法title()指定的操作即将每个单词的首字母改为大写

#print(name.upper())
#print(name.lower())
##将字符串全部改为大写或小写

##f字符串--format,每个变量都要用花括号，顺序引用变量的值
#first_name="ada"
#last_name="lovelace"
#full_name=f"{first_name} {last_name}"
#print(full_name)
#print(f"hello,{full_name.title()}!")

#message=f"hello,{full_name.title()}!"
#print(message)

#print("python")
#print("\tpython")#\t--表示空格（制表符）
#print("language:\npython\nc\njavascript")#\n--换行符
#print("language:\n\tpython\n\tc\n\tjavascript")

favorite_language='python '
print(favorite_language)#输出为‘python '
print(favorite_language.rstrip())#rstrip()--暂时删除字符串末尾的空白，下次询问时空白会再次出现

favorite_language=favorite_language.rstrip()#将结果关联到原来变量，可永久删除空白

#lstrip()--删除字符串开头空白，strip()--删除字符串两边空白
favorite_language=favorite_language.lstrip()
favorite_language=favorite_language.strip()