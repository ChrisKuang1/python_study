#双向链表实现
#创建一个节点元素类
class IntNode(object):
    def __init__(self, i, n, p):
        self.item = i
        self.next = n
        self.previous = p

#创建一个列表类
class SLList(object):
    def __init__(self, x=None):
        if x is None:
            #创建一个哨兵
            self.__sentry = IntNode(x, None, None)
            self.__size = 0
        else:
            first = IntNode(x, None, None)
            self.__sentry = IntNode(x, first, first)
            self.__size = 1

    def add_first(self, x):
        first = IntNode(x, self.__sentry.previous, None)
        if self.__size == 0:
            self.__sentry.next = first
            self.__sentry.previous = first
        else:
            self.__sentry.previous.previous = first
            self.__sentry.previous = first
        
        self.__size += 1

    def get_first(self):
        return self.__sentry.previous.item

    def add_last(self, x):
        last = IntNode(x, None, self.__sentry.next)
        if self.__size == 0:
            self.__sentry.next = last
            self.__sentry.previous = last
        else:    
            self.__sentry.next.next = last
            self.__sentry.next = last

        self.__size += 1

    def get_last(self):
        return self.__sentry.next.item

    def add(self, index, item):
        if index == self.size() - 1:
            self.add_last(item)
        else:
            tmp = self.__sentry.previous

            while tmp.next:
                if index == 0:
                    tmp_item = IntNode(item, tmp.next, tmp)
                    tmp.next.previous = tmp_item
                    tmp.next = tmp_item
                    break
                tmp = tmp.next
                index -= 1
        
        self.__size += 1

    def to_str(self):
        tmp = self.__sentry.previous
        list_str = str(tmp.item)

        while tmp.next:
            tmp = tmp.next
            list_str += ',' + str(tmp.item)

        return list_str
    
    def size(self):
        return self.__size


l = SLList()
l.add_first(10)
l.add_first(11)
l.add_last(155)
l.add(1, 20)
print(l.get_first())
print(l.to_str())
print(l.size())