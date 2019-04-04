# 自己实现链表
class IntList(object):
    def __init__(self, f, r):
        self.first = f
        self.rest = r
    
    #获取链表长度，通过递归实现
    """ def size(self):
        if self.rest is None:
            return 1
        else:
            return 1 + self.rest.size() """
    
    #获取链表长度，通过循环实现
    def size(self):
        p = self
        total_size = 0
        while p is not None:
            total_size += 1
            p = p.rest
        return total_size
    
    #获取链表元素
    def get(self, n):
        list_size = self.size() - 1
        p = self
        while n < list_size:
            p = p.rest
            n += 1
        return p.first

        """ if n == self.size() - 1:
            return self.first
        else:
            return self.rest.get(n) """
        
l = IntList(5, None)
l = IntList(10, l)
l = IntList(15, l)
l = IntList(20, l)

# print(l.rest.rest.first)
print(l.size())
print(l.get(1))