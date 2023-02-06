#定义函数
def hello(name):
    print("hello world",name)
#执行函数体代码---》条用函数
hello("lalala")

old = 2
print(id(old))
def change(old):
    old=10
    print(id(old))
change(2)
print(old)

my_list=[1,3,3,4,54,67]
def change_list(my_list):
    my_list.append(123)
    return my_list

change_list(my_list)
print(my_list)