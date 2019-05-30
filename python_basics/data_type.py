#同时赋值
x = y = z = 1
print(x + y + z)

#分别赋值
i,j,k=1,2,3
print(i,j,k)

#获取关键字列表
help('keywords')

#数字型 - 整型
a = 1
print(type(a))


#数字型 - 浮点型
b = 2.9
print(type(b))

#字符串，单引号和双引号都支持
c = 'Hello World'
print(type(c))

#列表(有序)，是可变的
lis = [1, 'two', 3.0, 'four']
print(type(lis))

#元组（有序），创建完后就不能再进行修改了,使代码更安全
arr = (1, "two", 3.0, "four")
print(type(arr))
#如果要定义只有一个元素的元组，必须加一个逗号来消除歧义，否则会变成其他类型
t = (1)
t2 = (1,)
print(type(t), type(t2))
#“可变”元组
change_t = ('a','b',['A','B'])
change_t[2][0] = 'X'
change_t[2][1] = 'Y'
print(change_t)

#字典（无序）
dic = {1:'one','a':'two'}
print(type(dic))

#集合，集合中的元素是不能重复的
set1 = {1,2,3,4,5}
print(type(set1))
set2 = set([1,3,4,5])
print(type(set2))

#布尔型
bln1,bln2 = True, False
print(type(bln1),type(bln2))

#强制转换数据类型，
print(int(b))
print(str(a))
print(float(a))

#python不支持字符串和数字类型自动转换运算
print('a' + str(1))
print(1 + int('23'))

#abs求绝对值
print(abs(-1))
