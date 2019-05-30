#集合，集合中的元素是不能重复的，是无序的，不能放入可变对象
set1 = {1,2,4,5,6}

#使用set方法创建集合
set2 = set([1,2,4,1,2,8,5,5])
print(set2)

#添加元素
set2.add(3)

#删除元素
set2.remove(3)

#使用&获取交集
print(set1 & set2)

#使用|获取并集
print(set1 | set2)

#使用-获取差集（set1中有但不再set2中的元素）
print(set1 - set2)

#使用^获取对称差集（在set1和set2中，但不同时存在于两个集合中的元素）
print(set1 ^ set2)
print((set1 | set2) - (set1 & set2))
print((set1 - set2) | (set2 - set1))

#set中不能放入可变对象
#set3 = {1,2}
#set3.add(['A',"B"])
#print(set3)

#set中可以放入tuple，但是这个tuple里面不能包含可变对象
set4 = {1,(1,2,3),}
#set5 = {(1,[2,3]),}
print(set4)