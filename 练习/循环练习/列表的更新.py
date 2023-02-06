'''
3.定义一个list,任意输入10个数字保存到list,然后按从小到大排序（冒泡排序），元组中元素可以修改？如何更新元组中元素？
'''
import random

list_one = []
import os
print(random.Random())
print(random.randint(12,56))
# shuijishu = random.randint(0,999)
for i  in range(10):
    if i <10:
        shuijishu = random.randint(0, 999)
        list_one.append(shuijishu)
        print(list_one)
    else:
        pass
# def shuji():
#     a = random.randint(0, 999)`
list_one.sort()
print(list_one)