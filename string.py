#字符串从左往右检索由0开始，从右往左检索由-1

#三引号也可以用于赋值字符串
a = '''hello baby
		Hello, world'''
print(a)

#len()函数返回字符串长度
print(len(a))

#检索字符
print(a[0],a[-1])

b='1234567890'
#截取字符串，返回n到m-1位置的字符
print(b[3:8])

#截取字符串，从n到m-1位置每相隔2位获取一个字符
print(b[1:6:2])

#反向截取字符串，从n到m+1位置的字符
print(b[6:1:-1])

#截取字符串，如果默认从头去到尾，可以把数值取消只保留冒号
print(b[::1])

c="AbcDeFG"
#转换大小写
print(c.lower(),c.upper())

#查找某个字符的第一个出现的位置
print(c.find('D'))

#替换字符
print(c.replace('De','CK'))

#统计某个字符出现的次数
print(c.count('D'))

#判断字符串中是否只包含字母
print(c.isalpha())

#判断字符串中是否只包含数字
print(c.isdigit())

#字符串是不可变的，不可以对其某个位置直接修改，包括replace方法
#a='hello world'
#a[0]='c'

#读取用户输入,input方法中可以输入文字，用于显示文本sublime暂时不支持，input输入的内容是一个字符串内容
#user_input=input('请输入>')
#print(user_input)
