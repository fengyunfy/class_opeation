"""
number数字类型
"""
import math
import random

num = 123.231
print("123",num)
# 数字的绝对值
num1 = -1.523
num_01 = abs(num1)
print(num_01)
#取数字的上入整数
num2 = math.ceil(num1)
num3 =12.5
print(num2,math.ceil(num3))
#取数字的下舍整数
print(math.floor(num2),math.floor(num3))
#随机取数字
num4 = random.random()
print(num4)
num5 = random.randint(12,15)
print(num5)
#四舍五入取数字
num6 = 123.123
num06 = round(num6,2)
print(num06)
#去掉小数部分
num7 = math.trunc(num6)
print(num7)

print(9%2) #取余
print((9//2))

"""
string字符串的字符数据类型
"""
# 截取部分字段
strl = "hello world!"
strl1 = strl[0:2]
print(strl1)

#取单个字符字符串中的第二个字符
print(strl[1])
#取多个字符  从开始位置截图长度为3对应的字符串
print(strl[:3])
#取单个字符  字符串中倒数第二个字符
print(strl[-2])
#取从第三个字符开始，截取后面所有的字符
print(strl[2:])
#截取前六个字符
print(strl[0:7])
#每隔两个字符进行截取
print(strl[::2])
#字符串反转:从右到左截取
print(strl[::-1])

#以指定的分隔符把seq中元素合并成一个新字符串   关联合并分隔符
strl2 = "qqwwweeerrttyuuiiassdf"
strl3 = "-".join(strl2)
print(strl3)

# 通过分隔符截取字符   通过分隔符返回列表数据
strl4 = strl3.split("-")
print(strl4)

a = "hello world!"
a1 = "-".join(a)
print(a1)
a2 = a1.split("-")
print(a2)

num11 = 1.12323
b1 = round(num11)
print(b1)
b2 = math.trunc(num11)
print(b2)
#随机取值
b3 = random.random()
print(b3)
b4 = random.randint(1,3)
print(b4)

#替换字符串
s1 = "qwe=qweq=qeqwew=qweq=weq=qwe=q=weqw"
s2 = s1.replace("qwe","123",3)
print(s2)



