# import datetime
#
# temp_date = datetime.datetime.now()  # 获取当前时间 年月日时分秒
# print(temp_date)
# date1 = (temp_date + datetime.timedelta(days=-1)).strftime("%Y%m%d")  # 获取当前日期的前一天日期
# date2 = (temp_date + datetime.timedelta(days=-2)).strftime("%Y%m%d")  # 获取当前日期的前两天日期
# date3 = (temp_date + datetime.timedelta(days=90)).strftime("%Y%m%d")  # 获取当前日期的前三天日期
# print("前一天的日期 date1: " , date1)
# print("前两天的日期 date2: " , date2)
# print("前三天的日期 date3: " , date3)
import math

group_list = ['Tom', 'Allen', 'Jane', 'William', 'Tony']
print(group_list[0:2])
print(group_list[1:4])
print(group_list[3:5])