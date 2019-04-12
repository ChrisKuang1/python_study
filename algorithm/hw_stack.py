#单身狗配对
""" 1. 所有参加活动的人都只排成一列，来参加活动的女生只会和排在队伍最后的男生配对。
2. 如果女生来到现场没有可以配对的男生则活动失败。
3. 如果最后有没有被领走的男生则活动也失败。 """
""" queue = input()
stack = []
result = True
for p in queue:
    if p == 'm':
        stack.append(p)
    else:
        if len(stack) == 0:
            result = False
            break
        else:
            stack.pop()
if len(stack) > 0:
    result = False

print(result) """

""" 为了让配对活动更加完善，本次活动还考虑了双方的性格，双方必须性格也一致才能完成配对。
本着女士优先的原则，来参加活动的女生可以直接配对，先到的男生必须先等待。而如果女生来到现场没有可以配对的男生则活动失败，如果最后有没有被领走的男生则活动也失败。
假设所有参加活动的人都只排成一列，来参加活动的女生只会和排在队伍最后的男生配对。
 """
queue_list = input().split(' ')
result = True
stack = []

for p in queue_list:
    if p.startswith('m'):
        stack.append(p)
    else:
        if len(stack) == 0:
            result = False
            break
        else:
            if stack[len(stack) - 1].endswith(p[1]):
                stack.pop()
            else:
                result = False
                break

if len(stack) > 0:
    result = False

print(result)