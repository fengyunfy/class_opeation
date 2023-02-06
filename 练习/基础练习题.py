info = ['xixi','haha','didi']
message = """
    ---------------------欢迎进入T666班学习管理系统-----------------------
请选择系统功能：
0：显示所有学员信息
1：添加一个学员信息
2：删除一个学员信息
3：修改一个学员信息
4：查询一个学员信息    
"""

def operation():
    input("请选择系统功能:")
def all_info():
    print(info)
def add_info():
    add_student = input("请输入新增的学员信息：")
    info.append(add_student)
    print(info)
def del_info():
    del_student = input("请输入需要删除的学员信息：")
    if info.count(del_student) > 0 :
        info.remove(del_student)
        print(info)
    else:
        print("不存在这个学员信息")
def modify_info():
    before_modify_student = input("请输入需要替换的学生名字：")
    after_modify_student = input("请输入修改后的学生名字：")
    if info.count(before_modify_student) > 0 :
        info.remove(before_modify_student)
        info.append(after_modify_student)
        print(info)
    else:
        print("这个学员信息不存在")
def  select_info():
    find_student = input("请输入需要查询的学员名字：")
    if info.count(find_student) > 0 :
        number = info.index(find_student)
        print("[]个学生处于第【】位".format(find_student,number))
    else:
        print("这个学员信息不存在")

def caozuo():
    print(message)
    a = input("请选择系统功能：")
    if a == '0':
        add_info()
        caozuo()
    elif a == '1':
        del_info()
        caozuo()
    elif a == '2':
        modify_info()
        caozuo()
    elif a == '3':
        select_info()
        caozuo()
    elif a == '4':
        all_info()
        caozuo()
    elif a == 'exit':
        print("成功退出系统！")
    else:
        print("不存在这个命令")
        caozuo()


caozuo()


