#字符串从左往右检索由0开始，从右往左检索由-1

#三引号也可以用于赋值字符串,用于多行的内容，简化不必要的转义字符
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

#%格式化, %d替换整数，%s替换字符串，%f替换浮点数，%x替换十六进制整数，%%表示%
print('Hello %s' % 'world')
print('Hi, %s, you have $%d.' % ('Chris', 10000))
print('%2d-%02d' % (3,1))
print('%.2f' % 3.1415926)
print('grow rate: %d%%' % 7)

#format格式化输出
movie_name = '流浪地球'
movie_score = 80
print('电影<<{}>>的评分是{},电影<<{}>>备受好评！'.format(movie_name,movie_score,movie_name))
print('电影<<{0}>>的评分是{1},电影<<{0}>>备受好评！'.format(movie_name,movie_score))
print('电影<<{name}>>的评分是{score},电影<<{name}>>备受好评！'.format(
	name=movie_name,
	score=movie_score))

#print可以利用逗号分隔进行输出
print('1024 * 768 =', 1024*768, '!')

#可以利用r''表示''内部的字符串默认不转义
print(r'\\\t\\')

#ord函数获取字符的整数表示，chr函数把编码转换为对应字符
print(ord('A'),ord('中'),chr(66),chr(25991))

#字符串在内存中以Unicode方式表示，但保存到磁盘或者用于传输时则转换成bytes
print('ABC'.encode('ascii'), '中文'.encode('utf-8'),b'ABC'.decode('ascii'),b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
#可以传入errors参数用于忽略在解析中遇到无法解析的字符
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
#如果换成了bytes，len函数统计的就是字节数
print(len(b'ABC'),len('中文'.encode('utf-8')),len(b'\xe4\xb8\xad\xe6\x96\x87'))
