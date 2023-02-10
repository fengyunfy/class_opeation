class people():
    fuse ="wwwwwwwww"  #类属性
    language = "cn"

    def __init__(self,name,country):
        print(f"我的名字：{name},我的国家{country}")
        self.name = name  #实例属性
        self.country = country   #实例属性

    def speak(self):
        print("中文")

    @staticmethod
    def static_method():
        print("类方法")

if __name__ == "__main__":

    dd = people("22",'2')
    dd.speak()
    print(dd.name)
    print(people.fuse)