#身高排序
""" 一共两行数据，第一行是一共有多少人，第二行是每次可以有多少人来拍照。假设所有人的身高都正好各不相同。
总人数不超过20人，一次拍照最多不超过6人。 """

def calculation(count, same_time, result):
    for i in range(count, 0, -1):
        result.append(i)
        if len(result) == same_time:
            print(result)
            result.pop()
            continue

        calculation(i - 1, same_time,result)

    if len(result) > 0:
        result.pop()

count = int(input())
same_time = int(input())

result = []
calculation(count,same_time,result)








