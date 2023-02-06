import time
#获取当前时间
now_time = time.time()
print(now_time)
#获取当前时间戳
now_time_tuple =time.localtime()
print(now_time_tuple)
#英文显示当前时间
en_time = time.asctime()
print(en_time)
#时间戳转换成时间元组
ch_time = time.localtime(now_time)
print(ch_time)
#时间元组转换成时间戳
ch_time_tuple = time.mktime(now_time_tuple)
print(ch_time_tuple)
#时间元组与字符串的转换
str_time = time.strftime("%Y:%m:%d %H:%M:%S",now_time_tuple)
print(str_time)
#应用
'''
生成自动化测试报告
'''
log_time = time.strftime("%Y_%m_%d_%H_%M_%S",now_time_tuple)
log_path = f'自动化测试报告{log_time}'
with open(log_path,'w+') as file:
    file.write("报告")

#时间格式的字符串转换为时间元组
time_tuple = time.strptime(str_time,"%Y:%m:%d %H:%M:%S")
print(time_tuple)
