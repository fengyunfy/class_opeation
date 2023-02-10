from class_test import people
dd =people("123",'23')
dd.speak()
"""
私有属性与私有方法
"""

#私有属性
# 属性名：__私有属性名
#私有方法
# 方法名：__私有方法名
"""
注：私有属性与私有方法只能通过类得内部进行使用，实例对象或类不可以再外部使用
但是可以通过这种格式进行调用：——————对象._类名+私有属性/私有方法
"""
class people():
    fuse = "qwe"
    __weight = 80

    def speak(self):
        print("我说中国话")
        print("你的体重是：", self.__weight)
        self.__test()
    def __test(self):
        print("这是一个私有方法")
        print("我的体重是：",self.__weight)

dd = people()
dd.speak()

print(dd._people__weight)
print(dd._people__test)