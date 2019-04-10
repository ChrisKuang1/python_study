#给定一组数字，将他们用链表的形式进行存储。另外再给一个数字，将它插入到链表的末尾。输出这个链表
#创建一个节点元素类
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

    def to_str(self):
        tmp = self.__first
        list_str = str(tmp.item)

        while tmp.next:
            tmp = tmp.next
            list_str += '->' + str(tmp.item)

        return list_str


list_str = input()
list_str2 = input()
lis = list_str.split(' ')

result_list = SLList(lis[0])

for item in lis[1:]:
    result_list.add_last(item)

result_list.add_last(list_str2)
print(result_list.to_str())
    