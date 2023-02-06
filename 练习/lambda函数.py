"""
函数嵌套
定义：在某个函数中调用了另一个函数
"""
# 1.调用函数嵌套
def a():
    print("hello a ")
def b():
    print("hello b")
    a()
# 嵌套的定义
def c():
    print("hello c")
    def d():
        print("hello d")
    d()
c()

# 匿名函数
#lambda函数

sum  = lambda n1,n2,n3:n1*n2*n3
print(sum(1,2,3))
#lambda函数只是一个表达式，函数体比def简单的多
# lambda 的主体是一个表达式，而不是代码块。只能在lambda表达式中封装有限的逻辑进去

"""
递归函数
定义：重复进行调用某个函数，直到不符合某个条件，就结束调用
"""

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
list1 = ["zhangyi","zhanger","zhangsan","zhangsi","zhangwu","zhangliu"]
# def sele():
#     for i in range(list1):
#         print(i)
for i in range(len(list1)):
    print(list1[i])

# a = input("请选择系统功能:")
# if a == 0:
#     sele()