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

    def revert(self, m, n):
        count = 0
        current = self.__first
        left_tmp, head_tmp = None, None

        while count<m-1:
            current = current.next
            count += 1
        
        if m == 0:
            #left_tmp = current
            head_tmp = current
            last_tmp = current
        else:
            left_tmp = current
            head_tmp = current.next
            current = current.next
            last_tmp = current
            count +=1

        current = current.next
        count += 1

        while count<=n:
            tmp_next = current.next
            current.next = last_tmp

            if count == n and left_tmp is not None:
                left_tmp.next = current

            last_tmp = current
            current = tmp_next
            count += 1
        
        head_tmp.next = current

        if m == 0:
            self.__first = last_tmp


    def to_str(self):
        tmp = self.__first
        list_str = str(tmp.item)

        while tmp.next:
            tmp = tmp.next
            list_str += '->' + str(tmp.item)

        return list_str

list_str = input()
revert_indexes = input()
lis = list_str.split(' ')
revert_list = revert_indexes.split(' ')

result_list = SLList(lis[0])

for item in lis[1:]:
    result_list.add_last(item)

result_list.revert(int(revert_list[0]), int(revert_list[1]))
print(result_list.to_str())