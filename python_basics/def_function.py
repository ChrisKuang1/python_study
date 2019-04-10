#函数的定义
#可以在定义时给函数指定默认值
def test_grade(name='李白', grade='95'):
    print(name + '的成绩是' + grade)

test_grade()
#通过名称指定传入参数的顺序
test_grade(grade = '80', name = '李信')

#全局变量
a = 1

def hello():
    #表示使用全局变量
    global a
    #默认在方法中是可以调用全局变量的
    print(a)
    #但如果没有使用global定义，在使用后再定义局部变量，这时编译器会报错
    #a = 2

hello()