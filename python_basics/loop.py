#while
number = [1,2,3,8,4,5,6]
odd = []
even = []

while len(number)>0:
    #pop - remove and return item at index
    numbers = number.pop()
    if numbers % 2 ==0:
        odd.append(numbers)
    else:
        even.append(numbers)
print(odd)
print(even)

#pass表示啥都不甘，占位语句。需要ctr+c强制退出死循环
""" while True:
    pass """

#for
student_list = ['李白','韩信','花木兰']
for index in range(len(student_list)):
    #end可以用来控制使用什么分隔并打印到同一行中
    print(student_list[index],end=',')
print("\n")
for index, value in enumerate(student_list):
    if index == 0:
        continue
    if value == '韩信':
        break
    print(index,value)

#range不是列表类型，可以使用list进行转换
print(type(range(0,10)))
#从0开始到9，每相隔2取值
print(list(range(0,10,2)))

dic = {'a':1, 'b':2, 'c':3}
for i in dic:
    print(dic[i])

#循环中else的使用
#注意：只有循环因循环条件不成立而自然结束时，else语句才会被执行，break中断时else语句不执行
for i in range(10):
    if i == 6:
        print(i)
        #break
else:
    print('end')