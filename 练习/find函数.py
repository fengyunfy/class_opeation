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