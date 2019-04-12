#栈的实现(ADT)，递归也是包含了栈的概念，先进后出
class Stack(object):
    def __init__(self):
        self.__data = []
    
    def push(self, x):
        self.__data.append(x)

    def pop(self):
        return self.__data.pop()

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())