strl = "hello world"
strl2 = 'hello'
strl3 = "123456789"
print(type(strl))
print(type(strl2))
#截取字符串中的某个字符，切片
"""
语法格式：变量[start:end:step]     含头不含尾，左闭右开 
start:开始索引值,索引值从左到右，从0开始;从右到左，从-1开始
end:结束索引值
step:步长 默认是1
"""
#取单个字符字符串中的第二个字符
print(strl[1])
#取多个字符  从开始位置截图长度为3对应的字符串
print("从开始位置截图长度为3对应的字符串：" , strl[0:3])
#取单个字符  字符串中倒数第二个字符
print("字符串中倒数第二个字符:" , strl[-2])
#取从第三个字符开始，截取后面所有的字符
print("第三个字符开始，截取后面所有的字符:" , strl3[2:])
#截取前六个字符
print(strl3[:6])
#每隔两个字符进行截取
print(strl3[::2])
#字符串反转:从右到左截取
print(strl3[::-1])

# string类型：字符串是不可变的字符类型
name="123"
print("name的物理位置：",id(name))
name="11111"
print("name的物理位置:",id(name))
print(name)
# 字符串的拼接
name = name +"123123"
print(name)
# \n ' " | 特殊符号
print("111\n222")
# 原符号输出 前面会加反斜杠（\）特殊符号转义
# 特殊符号，进行特定场景的输出
print("111\\n222")
print(r"D:\PyCharm_Project\class3\string类型.py")
print(R"D:\PyCharm_Project\class3\string类型.py")

"""
字符串格式化
"""
# 字符串格式表示方式一
print("%s%s,工作年限：%d欢迎进入自动化"%("你好","nihao",3))   #%占位符
# 字符串格式表示方式二
print("{}{},工作年限：{}欢迎进入自动化".format("你好","nihao",3))
print("{2}{1},工作年限：{0}欢迎进入自动化".format("你好","nihao",3))
# format的灵活性大一点
# 字符串格式表示方式三 f 字面量格式化
name = "你好"
q = "123"
year = "3"
print(f"{name}{q}年限{year}")

"""
字符串的常见函数
"""
#join(sep)
#以指定的分隔符把seq中元素合并成一个新字符串   关联合并分隔符
#一般用于路径的合并
join_str = "hello world"
str5 = "-".join(join_str)
print(str5)   #--->h-e-l-l-o- -w-o-r-l-d
str6 = "\\".join(join_str)
print(str6)

#spilt()
# 通过分隔符截取字符   通过分隔符返回列表数据
str7 = "qwe;23;123;dede;wewe"
str8 = str7.split(";")
print(str8)   #---》['qwe', '23', '123', 'dede', 'wewe']


#replace（原字符，新字符）
#替换字符串
str_old = "1234567"
str_new = str_old.replace("123","000")
print(str_new)

#find（查找字符，开始索引，结束索引）查找字符串返回开始的索引值，没有找到返回
str_find = "1234567888"
str_s = str_find.find("8")
print(str_s)
#index  查找字符串返回开始的索引值，没有找到报错
str_s1 = str_find.index("8")
print(str_s1)

#count（查询字符，开始索引，结束索引）  返回某个字符在指定范围出现的次数
str_s2 = str_find.count("8",1,3)
print(str_s2)

#startswith（匹配字符，开始索引，结束索引） 判断是否以某个字符开头
str_s3 = str_find.startswith("8",-1)
print(str_s3)

#endswith（匹配字符，开始索引，结束索引） 判断是否以某个字符结尾
str_s4 = str_find.startswith("8")
print(str_s4)

