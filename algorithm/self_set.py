class Set(object):

    def __init__(self, data=[]):
        self.__data = []
        for item in data:
            if item not in self.__data:
                self.__data.append(item)

    def add(self, x):
        if x not in self.__data:
            self.__data.append(x)

    def get_all(self):
        return self.__data

set1 = Set([1,3,2,1,5,232,3])
set1.add(8)
set1.add(1)
print(set1.get_all())