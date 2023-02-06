#调用嵌套
def a():
    print("hello a")
def b():
    print("hello b")
    a()
b()
#定义嵌套
def c():
    print("hello c")
    def d():
        print("hello d")
    d()
c()

#用例1：先登录--实现功能1
#用例2：先登录-实现功能2
def login():
    pass

def f1():
    login()