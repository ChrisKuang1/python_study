#小明买东西
#使用循环方式实现
""" #创建一个节点元素类
class IntNode(object):
    def __init__(self, i, n):
        self.item = i
        self.next = n

#创建一个列表类
class SLList(object):
    def __init__(self, x):
        #两个下划线表示把变量或者方法设置成私有
        self.__first = IntNode(x, None)
        self.__last = self.__first
        self.__second_last = None
        self.__count = 1
    
    def add_last(self, x):
        self.__second_last = self.__last
        self.__last = IntNode(x, None)
        self.__second_last.next = self.__last
        self.__count += 1
    
    def size(self):
        return self.__count

    def calculation(self, money):
        tmp = self.__first

        total_price = 0

        while tmp:
            total_price = int(tmp.item)

            if total_price == money:
                return True
            elif total_price > money:
                return False
            else:   
                tmp1 = tmp.next
                while tmp1:
                    total_price += int(tmp1.item)
                    if total_price == money:
                        return True
                    if total_price > money:
                        break
                    tmp1 = tmp1.next
            tmp = tmp.next
        else:
            return False

product_prices = input()
money = input()
prices_list = product_prices.split(' ')

result_list = SLList(prices_list[0])

for item in prices_list[1:]:
    result_list.add_last(item)

print(result_list.calculation(int(money))) """

#使用递归方式实现
def calculation(array, index, money):
    if money == 0:
        return True
    elif index == 0:
        return array[index] == money
    elif array[index] > money:
        return calculation(array, index - 1, money)
    else:
        return calculation(array, index - 1, money - array[index]) or calculation(array, index - 1, money)


product_prices = input()
money = int(input())
prices_list = product_prices.split(' ')

array = [int(i) for i in prices_list]

print(calculation(array, len(array) - 1, money))
#index = len(array) - 1

