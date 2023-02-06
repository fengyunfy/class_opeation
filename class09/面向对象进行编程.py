#定义类
# class people:
#     fuse = "yello" #属性一     定义属性
#     language = "cn" #属性二
#     #构造方法————————》再实例化时会自动调用这个方法
#     #什么时候会去重构构造方法-----用于初始化数据
#
#     def __init__(self,name,classname):  #构造方法
#         print("我是构造函数")
#         print(f'实例化了一个类她的名称{name}，她的班级{classname}')
#
#     #定义行为？说话，睡觉
#     def speak(self):
#         print("我会说中文")
#
# #DD 对象
# #hefan 对象
#
# "类的实例化——————》对象"
# DD = people("DD",'217')
# DD.speak()
# print("获取DD同学的特征",DD.language,DD.fuse)
#
#
# #初始化数据 名称：DD 班级：217



class people:
    fuse = "yello"
    guoji = "zg"
    language = "cn"

    def __init__(self):
        print("实例化了一个对象")
        name = "dd"
        classroom = "2117"
        
    def see(self):
        print("人会对事物进行观察")


dd = people()
print(dd.fuse)
dd.see()
