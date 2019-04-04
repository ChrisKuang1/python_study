import random
#随机获取20个0-99的整数并添加到列表中
x = [random.randint(0,100) for i in range(20)]
print(x)
#偶数列进行降序，奇数列不变
y = x[::2]
y.sort(reverse=True)
x[::2] = y
print(x)