class people():
    def speak(self):
        #self代表类的实例
        print("这是一个实例方法")

    @staticmethod
    def static_method():
        print("这是一个静态方法")

    @classmethod
    def class_method(cls):
        #参数cls--》代表类，类本身
        print("这是一个类方法")

'''
静态方法与类方法的区别
1.装饰器不同
'''

#人员的增加--》方法  实例
class TestClass():
    num = 0
    #属性班级人数
    @classmethod
    def addNum(cls):
        cls.num +=1
    def __init__(self):
        TestClass.addNum()
"""
    def getNum(self):
        return Class_test.num   #如果使用实例方法我就只能通过实例化后才能进行调用会不方便
"""



class student(TestClass):
    pass

a = student()
b = student()
c = student()
num = TestClass.num
print(num)

if __name__ =="__main__":  #用于调试代码，
    pass