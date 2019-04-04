#字典（无序），可变的
#字典中的key类型必须是不可变的，例如数值，字符串或元组

#如果key重复，以最后一个的数据为准
user1 = {'name':'李雷','numbers':'1234',"name":'李四'}
print(user1['name'])

#使用列表和元组的组合，创建字典
message = [('lilei',98),('hanmeimei',99)]
d = dict(message)
print(d)

#根据关键字参数新建字典
d1 = dict(lilei = 98, hanmeimei = 99)
d1['hanmeimei'] = 100
d1['madongmei'] = 90
print(d1)

#get方法获取某个key对应的值，如果该值不存在则返回指定的值
print(d1.get('123',0))

#删除字典某某个值
del d1['lilei']
print(d1)

#删除字典中所有值
d1.clear()
print(d1)

#删除字典本身
del d1

#由字典构成的列表
student1 = {'name':'李雷','age':'18','grade':98}
student2 = {'name':'韩信','age':'22','grade':80}
student3 = {'name':'李白','age':'28','grade':100}

student = [student1,student2,student3]

print(student)

#字典中存储列表
favorite_class = {'李雷':['数学','英语'], '韩信':['语文'], '李白':['语文','数学','地理']}
print(favorite_class)
print(favorite_class['李白'][0])

#字典中存储字典
class1 = {'No1':student1,'No2':student2,'No3':student3}
print(class1)
print(class1['No3']['name'])