#分段函数计算
""" x = int(input("Please input digit X: "))
if x<0:
    y = 0
elif x<5:
    y = x
elif x<10:
    y = 3 * x - 5
elif x<20:
    y = 0.5 * x - 2
elif x>=20:
    y = 0
else:
    print("Invalid Input!")
print("y is " + str(y)) """

#判断是否闰年
year = int(input("Please input year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(str(year) + "是闰年")
else:
    print(str(year) + "不是闰年")