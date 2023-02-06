"""
实现学生管理系统，完成对学院增删改查和退出学生管理系统
要求1：使用一个list用于保存学生得姓名
要求2：输入0显示所有学员的信息，1代表增加，2代表删除，3代表修改，4代表查询，exit代表退出
系统界面如下：
-----------------欢迎进入T666班学生管理系统---------------------------
#请选择系统功能：
0：显示所有学员信息
1：添加一个学员信息
2：删除一个学员信息
3：修改一个学员信息
4：查询一个学员信息
exit：退出学生管理系统
"""

list1 = ["张一","张二","张三","李一","李二"]
def info1():
    print(list1)

def add():
    add_name = input("请输入要添加的学生姓名：")
    list1.append(add_name)
    print(list1)

def delete1():
    delete_name = str(input("请输入要删除的学生姓名："))
    if list1.count(delete_name)>0:
        list1.remove(delete_name)
        print(list1)
    else:
        print("无")

def modify1():
    modify_name1 = str(input("请输入要修改的学生姓名："))
    modify_name2 = str(input("请输入修改后的学生姓名："))
    list1.remove(modify_name1)
    list1.append(modify_name2)
    print(list1)

def find1():
    index1 = str(input("请输入你要查询的学生名称："))
    print("{}的座位在{}".format(index1,list1.index(index1)))

def tuichu():
    print("您已退出学生管理系统")

message ="""
请选择系统功能：
0：显示所有学员信息
1：添加一个学员信息
2：删除一个学员信息
3：修改一个学员信息
4：查询一个学员信息
exit：退出学生管理系统
"""

#1.封装对应的函数，业务切割成多个函数 函数与函数之间独立
#2.执行对应的操作,需要循环的实现操作--》不同操作封装到一个函数---》递归函数

def caozuo(nr,infolist):
    if nr == "0":
        info1()
        caozuo(input(message),list1)
    elif nr == "1":
        add()
        caozuo(input(message),list1)
    elif nr == "2":
        delete1()
        caozuo(input(message),list1)
    elif nr == "3":
        modify1()
        caozuo(input(message),list1)
    elif nr == "4":
        find1()
        caozuo(input(message),list1)
    elif nr == "exit":
        tuichu()
    else:
        print("有误")
        caozuo(input(message),list1)

caozuo(input(message),list1)

