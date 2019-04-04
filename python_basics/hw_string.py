name = ' Alex '
print(name)
#移除 name 变量对应的值两边的空格，并输出移除后的内容
print(name.strip())  #.strip()移除指定字符串，空白，/t，/n等转义字符 
name=name.replace(' ','')
print(name)

#判断 name 变量对应的值是否以 "al"开头和以"X"结尾，并输出结果
print(name.startswith('al'),name.endswith('X'))
print(name[0:2] == 'al', name[-1] == 'X')

#将 name 变量对应的值中的 “l” 替换为 “p”，并输出结果
print(name.replace('l','p'))

#将 name 变量对应的值根据 “l” 分割，并输出结果
print(name[:name.find('l')],name[name.find('l')+1:])
print('|'.join(name)) #以某个字符拆分字符串

#将name变量对应的值分别变大写和小写，并输出结果
print(name.lower(),name.upper())
print(name.casefold()) #与lower方法一样
print(name.swapcase()) #大小写互换