#list是可变的
#list查找和插入的时间随着元素的增加而增加，但占用空间小，浪费内存很少

a = '123'

#把字符串转换成list
b = list(a)
print(b)

c=[1,2,3,4,5,6,7,8,9,0]
#截取列表,返回n到m-1位置组成的新列表，用法和字符串截取方法相同
print(c[2:6])

numbers = [1,5]
#使用新列表，从1号位开始进行替换添加
numbers[1:] = [8,9]
print(numbers)
#在n号位前插入列表数据，并最后保留从m号位开始的数据
numbers[1:2] = [2,3,4]
print(numbers)

#获取列表长度
print(len(numbers))

#修改某个位置的值
numbers[0] = "张三"
print(numbers)

#在列表后添加元素
inventory = ['钥匙','毒药']
inventory.append('解药')
print(inventory)

#在m的位置前插入值
inventory.insert(1,'你好')
print(inventory)

#删除某个位置的元素
#del inventory[0]
inventory.pop(0)
print(inventory)

#列表相加
num1 = [1,2,3,4,5]
num2 = [6,7,8,9,0]
print(num1 + num2)

#判断某个元素是否存在于列表中
if '解药' in inventory:
    print("yes")
else:
    print('no')

#获取列表中某个元素重复的次数
strList = [0,1,1,3,5,1,2]
print(strList.count(1))

#获取某个元素在列表中第一次出现的位置
print(strList.index(1))

#Test - 将字符串转换成列表后，对其偶数下标元素进行降序排列，基数下标元素不变
testList = list('132569874')
evenNum = testList[::2]
print(testList)
evenNum.sort(reverse=True)
testList[::2]=evenNum
print(testList)
