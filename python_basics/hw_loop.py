import random
#随机获取20个0-99的整数并添加到列表中
x = [random.randint(0,100) for i in range(20)]
print(x)
#偶数列进行降序，奇数列不变
y = x[::2]
y.sort(reverse=True)
x[::2] = y
print(x)

#求400万以内最大的斐波那契数，并求出是第几个斐波那契数
a, b = 2, 1
count = 1
while a<4000000:
    a, b = a+b, a
    count += 1
    
print(count, b)

#百钱买百鸡
for big in range(21):
    for medium in range(34):
        small = 100 - big - medium
        if small % 3 == 0:
            if 5*big + 3*medium + small//3 == 100:
                print(big, medium, small)
