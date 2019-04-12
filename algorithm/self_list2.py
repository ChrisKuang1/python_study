#链表实现
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
        self.__size = 1

    def add_first(self, x):
        self.__first = IntNode(x, self.__first)
        self.__size += 1

    def get_first(self):
        return self.__first.item

    def add_last(self, x):
        tmp = self.__first
        while tmp.next:
            tmp = tmp.next
        tmp.next = IntNode(x, None)
        self.__size += 1

    def get_last(self):
        tmp = self.__first
        while tmp.next:
            tmp = tmp.next
        return tmp.item

    def get(self, x):
        tmp = self.__first
        n = 0
        while n<x:
            n += 1
            tmp = tmp.next
        return tmp.item

    def to_str(self):
        tmp = self.__first
        list_str = str(tmp.item)

        while tmp.next:
            tmp = tmp.next
            list_str += ',' + str(tmp.item)

        return list_str

    #定义私有方法保护其中的算法
    def __count(self, p):
        if not p.next:
            return 1
        else:
            return 1 + self.__count(p.next)
    
    def size(self):
        return self.__count(self.__first)
        #return self.__size


l = SLList(5)
l.add_first(10)
l.add_first(11)
l.add_last(155)
print(l.get_first())
print(l.to_str())
print(l.get(2))
print(l.size())