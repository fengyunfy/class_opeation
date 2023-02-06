import math
import random
from math import ceil

a = 1000
b = -1000
c = 1.52
d = 1.23
e = 6.66

print('b的绝对值：', end=" ")
b1 = abs(b)
print(b1)

#若需要使用上入函数时，需要导入math的包
print('c的上入函数' , end=" ")
c1 = ceil(c)
print(c1)

print("d的下舍函数" , end=" ")
d1 = math.floor(d)
print(d1)

print('随机生成一个【0，1）之间的数字：',random.random())
print('随机生成一个【12,15】的数字', random.randint(12,15))

#四舍五入使用round函数
e1 = round(e)
print(e1)

#去掉数字的整数部分---取整
e2 = math.trunc(e)
print('取整E：', e2 )


'''
常用的数字函数--总结
取绝对值  abs()
取整数   trunc()   注意该函数需先导入math包，才能使用
取数值的上入整数   ceil() 注意该函数需先导入math包，才能使用
取数值的下舍整数   floor() 注意该函数需先导入math包，才能使用
取数值的四舍五入   round() 
取[0,1)之间的随机数   random.random()  注意使用该函数需导入random包
取(a,b)之间的整数     random.randint() 注意使用该函数需导入random包
'''