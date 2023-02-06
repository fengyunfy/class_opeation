#定义一个数字类型
import random

num1 = 1
num2 = 2.1
num3 = False
print(type(num1))
print(type(num2))
print(type(num3))
print(num1**2)
print(9/2)
#两个斜杠 // 取整数部分，不会进行四舍五入
#一个斜杠 / 会返回小数
print(9//2.0)
import math
print(abs(-22),math.floor(1.2324),math.ceil(5.1))
print("floor(x)返回的是数字的下舍整数:",math.floor(3.1215))
print("ceil(x)返回的是数字的上如整数，",math.ceil(5.123))
print("random.random(a,b)返回随机生成的一个实数，它在[0,1)范围内:",random.random())
print(random.randint(1,4))
#四舍五入
print(round(5.6),round(5.65,1))
print(round(2.5))
#去掉整数部分
print(math.trunc(5.6))

print(isinstance(num1,int))