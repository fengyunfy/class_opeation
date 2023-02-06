import os
import time
"""
时间戳
Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能

"""
# Python函数用一个元组装起来的9组数字处理时间
# 序号	字段	        值
# 0	    4位数年	    2008
# 1	    月	        1 到 12
# 2	    日	        1到31
# 3	    小时	        0到23
# 4	    分钟	        0到59
# 5	    秒	        0到61 (60或61 是闰秒)
# 6	    一周的第几日	0到6 (0是周一)
# 7	    一年的第几日	1到366 (儒略历)
# 8	    夏令时	    -1, 0, 1, -1是决定是否为夏令时的旗帜

#当前时间戳--->1970-1-1 00:00:00 到当前时间的的秒数
a = time.time()
print(a)
#获取现在的时间元组--->time.struct_time(tm_year=2022, tm_mon=9, tm_mday=22, tm_hour=21, tm_min=39, tm_sec=2,
# tm_wday=3, tm_yday=265, tm_isdst=0)
#当前时间元组
b = time.localtime()
print(b)
# 获取当前时间的年份如何获取
c = b[0]
print(c)
month = b.tm_mon
print(month)
year = b.tm_year #时间戳指1970年1月1日00：00：00到如今的总秒数
print(year)
weekday = b.tm_wday
print(weekday)
#英文方式显示时间
print(time.asctime())

#时间戳转化为时间元组
d = time.localtime(1663854375.217798)
print(d)
#时间元组转化为时间戳
e = time.mktime(d)
print(e)

#时间元组转化为字符串
f = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(f)
#输入日志/报告  文件名称后面加上时间
path1 = f'log_{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())}'
print(path1)
try:
    with open(path1,"w") as file:
        file.write("开始写入内容")
        print(file.read())
except:
    print("发生错误")
#字符串转化成时间
B = time.strptime(f,"%Y-%m-%d %H:%M:%S")
print(B)

"""
总结：
时间戳  到当前时间的总秒数
常用函数
"""

